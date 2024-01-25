# WordNet Parser
This parsing project is designed for the lexical semantics domain, focusing on extracting and organizing words and their relationships from [en-word.net](https://en-word.net)'s English WordNet dataset ```english-wordnet-2023.xml```. The parser systematically processes the XML file, collecting lexical entry and synset information and generating a CSV output that encapsulates word relationships, relations, and related words in the format:
```WordA,relation,WordB```.

## Workflow
```
Start timer
Load each of the 120K unique Synsets from the input XML file into a Synset map:
      For each Synset id, add the Synset node to the Synset map
      Increment parsedRows counter for Synset, keeping track of the number of rows parsed

Load each of the 161K unique LexicalEntrys from the input XML file:
      Load each of the 212K unique Senses into a Sense map:      
            For each Sense id, add the Sense synset to the map
            Increment parsedRows counter for Sense, keeping track of the number of rows parsed

      Increment parsedRows counter for Lemma and Form, keeping track of the number of rows parsed
            
Increment parsedRows counter for SyntacticBehaviour, keeping track of the number of rows parsed

Open output CSV file

Find the Synset for each LexicalEntry’s Sense child(ren):
      Get the Lemma writtenForm
      Increment totalWord counter

      For each Sense, find the Sense synset in the Synset map:
            The Sense synset should be a Synset id, a Synset should be found
            For each SynsetRelation:
                  Get the SynsetRelation target
                  Get the SynsetRelation relType
                  Find the SynsetRelation target in the Synset map:
                        The SynsetRelation target should be a Synset id, a Synset should be found
                        For each member in the Synset members:
                              Save one line to the output file with the format: writtenForm, relType, member
                              Increment outputRow counter
            
Find the Synset for each LexicalEntry’s SenseRelation grandchild(ren):
      Get the Lemma writtenForm
      For each Sense, iterate over each of the SenseRelations:
            Get the SenseRelation target
            Find the SenseRelation target in the Sense map:
                  The SenseRelation target should be a Sense id, a Sense should be found
                  Find the Sense synset in the Synset map, a Synset should be found
                  For each member in the Synset members:
                        Save one line to the output file with the format: writtenForm, relType, member
                        Increment outputRow counter
            
Close output CSV file
Stop timer

Print summary to console:
      Total rows parsed: parsedRows counter
      Total words: totalWord counter
      Total output rows: outputRow counter
      Time spent: stop timer - start timer
```
## Requirements
### pugixml library:
* The program utilizes the pugixml library for XML parsing.
* You can find the library at: [pugixml GitHub repository](https://github.com/zeux/pugixml).
* Follow the instructions on the repository to download and install the library.

## Results
### Summary
* Total unique WordA: 150,730
* Total WordA-WordB pairs: 1,458,884
* Running time: 29,228 ms

### Time and space complexities
* ```O(e * s * r * m)``` for *e* lexical entries, *s* senses, *r* synset relations, and *m* members.
* ```O(t) + O(w) + O(l)``` for *t* number of stored entries, *w* output rows written, and maximum size *l* of local variables.

## Test procedure
### Prepare Test Data:
* Ensure the XML file contains a variety of lexical entries, senses, and relationships for comprehensive testing.

### Run the Program:
* Execute the compiled program in ```WordNetParser.cpp```.

### Verify Output:
* Check the ```results.csv``` file for the generated word-relation outputs.
* Verify that the relationships and data extracted align with expectations.

## Future improvements
### Separation of Concerns:
* Identify distinct functionalities in the code, such as loading XML, collecting synsets, and iterating over entries.
* Create separate functions or classes for each identified functionality.

### Reduce code duplication:
* Identify common logic between the two sections where entry iteration occurs.
* Create a separate function for the common logic.

### Time complexity:
* Evaluate whether using iterators directly can improve performance, particularly in nested loops where XML nodes are accessed.
* Replace ```next_sibling``` with iterator-based approaches where applicable, potentially reducing time complexity.

### Magic number code smells
* Define named constants or variables for magic numbers to improve code readability and maintainability.
