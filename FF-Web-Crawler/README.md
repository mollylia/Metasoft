# Ford Foundation Web Crawler
## How to deploy
### Prerequisites
Before deploying the web crawler, ensure you have the following prerequisites installed:
1. Python
    * Visit the official [Python website](https://www.python.org) to download Python.
    * During installation, ensure to check the option that says "Add Python to PATH".
    * Verify the installation by opening a command prompt or terminal and typing ```python --version``` or ```python3 --version```.
    * Verify **pip** is installed by typing ```pip --version``` or ```pip3 --version``` in the command prompt or terminal.


2. Frameworks and libraries
    * Install Scrapy, Beautiful Soup, and Scrapy Selenium by running the following commands:
   
      ```
      # Install the frameworks and libaries with pip
      
      $ pip install scrapy
      $ pip install beautifulsoup4
      $ pip install scrapy-selenium
      
      
      # Install the frameworks and libaries with pip3
      
      $ pip3 install scrapy
      $ pip3 install beautifulsoup4
      $ pip3 install scrapy-selenium
      ```

### Deployment steps
1. Navigate to the project directory ```FF-Web-Crawler```.
2. Change to the ```fordfoundationcrawling``` directory within the project directory.
3. Run the script using the following command:
   ``` 
   $ scrapy crawl foundationsearch
   
   
   # Run this command to save the results from 'yield' in the parse_item method
   # The results will be saved to a JSON file called output.json
   
   $ scrapy crawl foundationsearch -o output.json
   ```
