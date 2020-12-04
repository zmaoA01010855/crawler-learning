# Crawler-learning
Personal learning path of web crawler based on Guang Chen's [GitHub] of Python Programming courses.

## Prerequisite
  - [Python 3]
  - [Anaconda] for Python env management with visualization (or any venv you want to setup)
  - re lib for regular expression
  ```sh
  pip install regex
  ```
  - lxml lib for xpath tree
  ```sh
  pip install lxml
  ```

## Some useful tools you might need
  - [RegExr] - an online regular expression builder.
  - [XPath Cheatsheet] - XPath syntax infomation sheet.
  - [XPath helper] - a Chrome extension for locating the xpath of certain element.
  - [You-Get] - media content downloader.
  - [Curl to Python] - converting curl command to python codes and gaining request header infomation from client's browser.


## Learning Contents
### Basic Python implementation for a web crawler class
  - MyCrawler class
  - 3 steps: download, extract, save.
  - With serveral oo design concepts: encapsulation, abstract, inheritance).
  - Using requests lib: get() & post()

### Exercise 1: Retrieving book list info from Douban Reading Page with Regex:
  - Creating DoubanCrawler class extending MyCrawler class.
  - Finding the book infomation pattern on HTML page by using Regex.
  - Implementing the logic of extraction.
  - Finding if the agent infomation in request header needs to be changed.

### Exercise 2: Retrieving book list info from Douban Reading Page with XPath:
  - Finding the book infomation pattern on HTML page using XPath.
  - Coverting response string to HTML Tree
  - Implementing the logic of extraction.
  - Finding if the agent infomation in request header needs to be changed.


## License
MIT

## Reference
  - Guang Chen, PhD, Associate Professor of BUPT
  - Guang Chen's [GitHub] of Python Programming courses.


[Anaconda]: <https://www.anaconda.com/products/individual>
[Python 3]: <https://www.python.org/downloads/>
[RegExr]: <https://regexr.com/>
[XPath Cheatsheet]: <https://devhints.io/xpath>
[XPath helper]: <https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl>
[You-Get]: <https://you-get.org/>
[Curl to Python]: <https://curl.trillworks.com/>
[GitHub]: <https://github.com/fly51fly/Practical_Python_Programming>
