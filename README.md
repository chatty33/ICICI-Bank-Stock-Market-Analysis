# ICICI-Bank-Stock-Market-Analysis

#Overview#
This project is an algorithmic trading application developed by Gowtham to perform stock market analysis on ICICI Bank. It stores real-time stock market data of ICICI Bank for each day of the week, from 11.15 AM to 2.15 PM, with a 15-minute delay using the Yahoo Finance library. The data is stored in a MongoDB database.

Requirements
Python 3.x
yfinance library
apscheduler library
pymongo library
Install the required libraries using:

pip install yfinance apscheduler pymongo

How it Works
The program fetches the stock market data for ICICI Bank from Yahoo Finance using the yfinance library. It retrieves the 15-minute candle data for each day from 11.15 AM to 2.15 PM. The data is then stored in a MongoDB database.

The APScheduler library is used to schedule the data retrieval process. The program runs daily, and due to the 15-minute delay in Yahoo Finance, it starts logging at 11.15 AM to capture data for the 11.00 AM time interval.
