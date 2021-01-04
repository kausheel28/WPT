# WPT Metrics Extraction
Extraction of WPT Metrics by taking mutliple WPT Results URL as an input in .txt file

A lot of time and manual effort is put into extraction of important web vitals from UI of Web Page Test (WPT) tool used for measuring and analyzing the performance of multiple websites and user journeys and documenting into excels

This python script which allows to scrape data from WPT's UI by just providing the URLs of test execution in a .txt file, automatically filling the values into a spreadsheet

The scripts reads each url present in .txt file and extracts the table contents and store it in data frame. code can be optimised according to your requirement to perform operations on data frame like multiplying each column with certain value or getting averages of certain columns and exporting the data frames to new sheet in excel file.

# Requirements
Install Python 3.8.5


Import the following libraries using the command: pip install <lib-name>
  
  
1.pandas


2.requests


3.openpyxl


  
# Setup
Place WPT.py file in Python Folder


Create a text file which consists of WPT Results URL's place it in Python folder


Create a Excel file to export the results and Place it in the above mentioned folder


Open WPT.py file in any text editor like notepad++ and change the textfile and excel file paths accordingly and save.



# Steps to run
Open cmd and navigate to Python folder


Run command: python WPT.py
