# WPT Metrics Extraction
Extraction of WPT Metrics by taking mutliple WPT Results URL as an input in .txt file

A lot of time and manual effort is put into extraction of important web vitals from UI of Web Page Test (WPT) tool used for measuring and analyzing the performance of multiple websites and user journeys and documenting into excels

This python script which allows to scrape data from WPT's UI by just providing the URLs of test execution in a .txt file, automatically filling the values into a spreadsheet

The scripts reads each url present in .txt file and extracts the table contents and store it in data frame. code can be optimised according to your requirement to perform operations on data frame like multiplying each column with certain value or getting averages of certain columns and exporting the data frames to new sheet in excel file.
