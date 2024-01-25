#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>
#include <chrono>
#include "pugixml.hpp"

using namespace std;
using namespace pugi;
using namespace chrono;

int totalWordCount = 0;

vector<string> getMembers(string list) {
	string members = list;
	string member;
	stringstream sstream(members);
	vector<string> memberList;

	// Add individual member from members to vector
	while (getline(sstream, member, ' ')) {
		memberList.push_back(member);
	}

	// Remove unnecessary chars (oewn- and -n, -a, ...)
	for (int i = 0; i < memberList.size(); i++) {
		string member = memberList[i];
		member = member.substr(5, member.length() - 7);
		memberList[i] = member;
	}

	return memberList;
}

int main() {
	xml_document doc;
	unordered_map<string, xml_node> synsetMap;                             // map<synsetId, synset node>
	unordered_map<string, string> senseMap;                                // map<senseId, senseSynset>

	int parsedCounter = 13;
	int totalOutputRows = 0;
	const char* fileName = "english-wordnet-2023.xml";

	auto start = high_resolution_clock::now();
	cout << "Loading XML: " << fileName << endl;

	// Load XML file
	xml_parse_result result = doc.load_file(fileName);
	if (!result) {
		cerr << "Error loading XML file: " << result.description() << endl;
		return -1;
	}

	cout << "Collecting synset... " << endl;

	// Store synset id and synset node from Synset in map
	xml_node root = doc.child("LexicalResource").child("Lexicon");
	for (xml_node synset = root.child("Synset"); synset; synset = synset.next_sibling("Synset")) {
		parsedCounter += 2;
		string synsetId = synset.attribute("id").value();
		synsetMap[synsetId] = synset;

		// Iterate over synsets and increment counter
		for (xml_node synChild = synset.first_child(); synChild; synChild = synChild.next_sibling()) { parsedCounter++; }
	}

	cout << "    " << parsedCounter << " collected" << endl;
	cout << "Collecting sense... " << endl;

	// Store sense id and synset from LexicalEntry to map
	for (xml_node entry = root.child("LexicalEntry"); entry; entry = entry.next_sibling("LexicalEntry")) {
		parsedCounter += 2;

		for (xml_node sense = entry.child("Sense"); sense; sense = sense.next_sibling("Sense")) {
			string senseId = sense.attribute("id").value();
			string senseSynset = sense.attribute("synset").value();
			senseMap[senseId] = senseSynset;

			// Iterate over Sense child nodes and increment row counter
			if (sense.first_child()) {
				parsedCounter += 2;
				for (xml_node srelation = sense.first_child(); srelation; srelation = srelation.next_sibling()) { parsedCounter++; }
			} else { parsedCounter++; }
		}

		// Iterate over Lemma child nodes and increment row counter
		xml_node lemma = entry.child("Lemma");
		if (lemma. first_child()) {
			parsedCounter += 2;
			for (xml_node lchild = lemma.first_child(); lchild; lchild = lchild.next_sibling()) { parsedCounter++; }
		} else { parsedCounter++; }

		// Iterate over Form and increment row counter
		for (xml_node form = entry.child("Form"); form; form = form.next_sibling("Form")) { parsedCounter++; }
	}

	cout << "    " << parsedCounter << " collected" << endl;
	cout << "Iterating SyntacticBehaviours... " << endl;

	// Iterate over SyntacticBehaviour and increment row counter
	for (xml_node sbehaviour = root.child("SyntacticBehaviour"); sbehaviour; sbehaviour = sbehaviour.next_sibling("SyntacticBehaviour")) { parsedCounter++; }
	cout << "    " << parsedCounter << " collected" << endl;

	// Open output CSV file
	cout << "Output file = results.csv" << endl;
	ofstream outputFile("results.csv");

	// Iterate over LexicalEntries
	cout << "Iterating over LexicalEntries..." << endl;
	for (xml_node entry = root.child("LexicalEntry"); entry; entry = entry.next_sibling("LexicalEntry")) {
		string wordA = entry.first_child().attribute("writtenForm").value();
		totalWordCount++;

		if ((totalWordCount % 10000) == 0)
			cout << "    " << totalWordCount << ": " << wordA << endl;

		for (xml_node sense = entry.child("Sense"); sense; sense = sense.next_sibling("Sense")) {
			string synsetId = sense.attribute("synset").value();

			// Find entry's synset node
			auto synsetNodeIterator = synsetMap.find(synsetId);
			if (synsetNodeIterator != synsetMap.end()) {
				xml_node synsetNode = synsetNodeIterator->second;

				// Iterate over SynsetRelations
				for (xml_node srelation = synsetNode.child("SynsetRelation"); srelation; srelation = srelation.next_sibling("SynsetRelation")) {
					// Get target synset and relType/relationCode
					string targetSyn = srelation.attribute("target").value();
					string rtype = srelation.attribute("relType").value();

					// Find target node
					auto targetSynsetIterator = synsetMap.find(targetSyn);
					if (targetSynsetIterator != synsetMap.end()) {
						xml_node targetNode = targetSynsetIterator->second;
						string members = targetNode.attribute("members").value();

						// Get the members and write to output file
						vector<string> memberList = getMembers(members);
						for (int i = 0; i < memberList.size(); i++) {
							totalOutputRows++;
							outputFile << wordA << "," << rtype << "," << memberList[i] << endl;
							//outputFile << wordA << "," << relation << "," << memberList[i] << endl;
						}
					}
				}
			}
		}
	}

	cout << "   totalOutputRows = " << totalOutputRows << endl;

	// Find sense relation target nodes
	cout << "Finding sense relation target nodes..." << endl;
	int targetNodeCount = totalWordCount;

	for (xml_node entry = root.child("LexicalEntry"); entry; entry = entry.next_sibling("LexicalEntry")) {
		string wordA = entry.first_child().attribute("writtenForm").value();

		for (xml_node sense = entry.child("Sense"); sense; sense = sense.next_sibling("Sense")) {
			for (xml_node srelation = sense.first_child(); srelation; srelation = srelation.next_sibling("SenseRelation")) {
				string rtype = srelation.attribute("relType").value();
				string target = srelation.attribute("target").value();

				// Find corresponding sense id for sense relation target
				auto targetSenseIterator = senseMap.find(target);
				if (targetSenseIterator != senseMap.end()) {
					string targetId = targetSenseIterator->second;

					auto targetSynsetIterator = synsetMap.find(targetId);
					if (targetSynsetIterator != synsetMap.end()) {
						xml_node targetNode = targetSynsetIterator->second;
						string members = targetNode.attribute("members").value();

						targetNodeCount++;
						if ((targetNodeCount % 10000) == 0)
							cout << "    " << targetNodeCount << ": " << wordA << endl;

						// Get the members and write to output file
						vector<string> memberList = getMembers(members);
						for (int i = 0; i < memberList.size(); i++) {
							totalOutputRows++;
							outputFile << wordA << "," << rtype << "," << memberList[i] << endl;
						}
					}
				}
			}
		}
	}

	outputFile.close();

	cout << "   totalOutputRows = " << totalOutputRows << endl;
	auto stop = high_resolution_clock::now();
	auto duration = duration_cast<milliseconds>(stop - start);

	cout << "\nTotal rows parsed: " << parsedCounter << endl;
	cout << "Total words: " << totalWordCount << endl;
	cout << "Total output rows: " << totalOutputRows << endl;
	cout << "Time spent: " << duration.count() << " ms";

	return 0;
}