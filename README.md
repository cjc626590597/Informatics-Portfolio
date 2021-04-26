# Mobile Phone Recommendation Web Application



## About

This project is intended to build a mobile phone recommendation web application. This web application recommend mobile phone to users in terms of the mobile phone parameters set by users. However, although some mobile phones have the same parameters, they may still have different usages due to some other factors. In order to make users buy more suitable mobile phones, this web application uses decision tree to analyze the usage ('Game', 'Business', 'Photography', 'Multi-purpose' & 'None') of mobile phones. This web application will show both mobile phone parameters and their usages to give users better idea to buy more suitable mobile phones.



## Environment Requirements

Python version: Python 3.8

Operating system: Windows 10 (64 bit)

Libraries (This is included in 'requirements.txt') :

Install following libraries manually

Or 

Use command 'pip3 install -r requirements.txt' in project root directory to install.

```python
beautifulsoup4==4.9.1
bs4==0.0.1
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
Flask==1.1.2
Flask-MySQL==1.4.0
Flask-SQLAlchemy==2.4.4
Flask-WTF==0.14.2
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
numpy==1.20.2
pandas==1.2.4
PyMySQL==1.0.2
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2021.1
requests==2.25.1
six==1.15.0
soupsieve==2.0.1
SQLAlchemy==1.3.6
urllib3==1.26.4
Werkzeug==0.16.0
WTForms==2.2.1
xlrd==2.0.1
xlwt==1.3.0
```



## How to use

### 1. Scrape (This is a command line operate)

Go to 'website/scraping' in command line.

If you want to scrap URLs of all phones, execute python script 'scrapURL.py' and a new excel file 'URLs.xls' including all phone URLs is created. 

If you want to scrap required parameters  of all phones, execute python script 'scrapData.py' and a new excel file named 'firstData.xls' including all phone parameters is created. 

If you want to clean the phone data, execute python script 'dataCleaning.py' and a new excel file named 'secondData.xls' including cleaned data is created. 

If you want to further clean the phone data to remove the characters not required, execute python script 'dataCleaning_range.py' and a new excel file named 'lastData.xls' is created.

(Sometimes, for some unexpected data, you need to open the excel file and clean them manually) 


### 2. Upload Data (This is a command line operate)

Move excel files from 'scraping' directory.

Go to 'website/database' in command line.

If you want to new phones to database, modify the name of excel file to 'newData.xls' and execute python script 'uploadNewData.py'. 

If you want to add data for training decision tree, add data in new excel file to 'decisionTree/Data/trainingData.xls'. 

If you want to add data for testing decision tree, add data in new excel file to 'decisionTree/Data/testingData.xls'. 



### 3. Run Website (This is a command line operate)

Go to root directory of this project in command line and run 'flask run'.

Open http://127.0.0.1:5000/ in browser.



### 4. Choose phone parameters (This is GUI operate)

*Use VPN to connect to Cardiff University MySQL Database.

Open http://127.0.0.1:5000/ in browser.

Choose phone parameters via drop down box and click 'Search' button.

*After click the 'Search' button, you may need to wait for a very long time if there is not excel with training data in your local directory. Because the program will retrieve training data from database to build the decision tree.



### 5. Export Structured Files (This is GUI operate)

Click 'Export HTML' button or 'Export JSON-LD' button to export structured file.

Choose directory to save structured file in saving window.



## Directory Structure

```
Informatics-Portfolio
|-- Project
    |-- README.md
    |-- requirements.txt
    |-- wsgi.py
    |-- website
        |-- __init__.py
        |-- app.py
        |-- forms.py
        |-- functions.py
        |-- models.py
        |-- routes.py
        |-- database
        |   |-- models.py
        |   |-- uploadNewData.py
        |   |-- uploadTestData.py
        |   |-- uploadTrainingData.py
        |-- decisionTree
        |   |-- decisionTree.py
        |   |-- data
        |       |-- testData.xls
        |       |-- trainingData.xls
        |-- export
        |   |-- export.py
        |   |-- phones.jsonld
        |   |-- phones.html
        |-- scraping
        |   |-- dataCleaning.py
        |   |-- dataCleaning_range.py
        |   |-- scrapData.py
        |   |-- scrapURL.py
        |   |-- utils
        |       |-- askHtml.py
        |   |-- data
        |       |-- URLs.xls
        |       |-- firstData.xls
        |       |-- sencondData.xls
        |       |-- lastData.xls
        |-- static
        |   |-- Image
        |   |   |-- left.png
        |   |   |-- line.png
        |   |   |-- phone.png
        |   |   |-- right.png
        |   |-- JavaScript
        |   |   |-- result.js
        |   |-- Stylesheets
        |       |-- index.css
        |       |-- result.css
        |-- templates
            |-- index.html
            |-- result.html
```

| File or directory name   | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| README.md                | It is this document telling you how to use this project      |
| requirements.txt         | It is mentioned above                                        |
| wsgi.py                  | It is created for 'flask run'                                |
| website (Directory)      | This is main directory for web application source code       |
| \_\_init\_\_.py          | It is used to initialize flask setting like database and csrf |
| app.py                   | App object for flask is created here                         |
| forms.py                 | This is used for form to select phone parameters             |
| functions.py             | This is used to search phones in database                    |
| models.py                | This is models for phones                                    |
| routes.py                | This is about URL and redirection in flask                   |
| database (Directory)     | This directory includes python scripts for uploading data to database |
| decisionTree (Directory) | This directory includes decision tree and some data          |
| decisionTree.py          | This includes code for creating decision tree and predict result |
| testData.xls             | This is used to test decision tree                           |
| trainingData.xls         | This is used to build decision tree                          |
| export (Directory)       | This directory includes python script for exporting structured files |
| phones.jsonld            | JSON-LD file for phones                                      |
| phones.html           | HTML file for phones                                       |
| scraping (Directory)     | This directory includes python script for scraping data from website |
| dataCleaning.py:         | This is used to clean the phone data  |
| dataCleaning_range.py:   | This is used to further clean the phone data |
| scrapData.py:            | This is used to scrap parameters of all phones |
| scrapURL.py:             | This is used to scrap URLs of all phones                     |
| utils (Directory)             | This directory includes common functions |
| askHtml.py:              | This is a function used to scrap html content of a website |
| data (Directory)          | This directory includes scraped data |
| URLs.xls | This is an example of scraped URLs |
| firstData.xls | This is an example of scraped parameters of 9 phones         |
| secondData.xls | This is an example of scraped phones parameters after first data cleaning |
| lastData.xls | This is an example of scraped phones parameters after second data cleaning |
| static (Directory)       | This directory includes files for website front end.         |
| index.css                | This is the search page style                                |
| index.html               | This is the search page                                      |
| result.css               | This is the result page style                                |
| result.html              | This is the result page                                      |



## Authors

| Student ID | Student Name  |
| ---------- | ------------- |
| 2086697    | Yongyi Wu     |
| 2086698    | Jingyi Zhang  |
| 2096406    | Yunlong Feng  |
| 2097255    | Chengtian He  |
| 2097505    | Juncheng Chen |

