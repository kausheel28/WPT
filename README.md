# WPT Metrics Extraction
Extraction of WPT Metrics by taking mutliple WPT Results URLs as an input in .txt file

A lot of time and manual effort is put into extraction of important web vitals from UI of Web Page Test (WPT) tool used for measuring and analyzing the performance of multiple websites and user journeys and documenting into excels

This python script which allows to scrape data from WPT's UI by just providing the URLs of test execution in a .txt file, automatically filling the values into a spreadsheet

The script reads each url present in .txt file and extracts the table contents and stores it in data frame. The Code can be optimised according to your requirement to perform operations on data frame like multiplying each column with certain value or getting averages of certain columns and exporting the data frames to new sheet in excel file.

# Requirements
Install Python 3.7 or above


Import Important Libraries by running the following Commands:
  
  
1.pip install pandas


2.pip install requests


3.pip install openpyxl


4.pip install lxml


  
# Setup
Place WPT.py file in Python Folder


Create a text file which consists of WPT Results URL's and place it in Python folder


Create an Excel file to export the results and place it in the Python folder


Open WPT.py file in any text editor like notepad++ and change the textfile and excel file paths accordingly and save.



# Steps to run
Open cmd and navigate to Python folder


Run command: python WPT.py
