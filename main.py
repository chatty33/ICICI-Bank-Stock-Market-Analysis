import yfinance as yf
import pymongo
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# Establish MongoDB connection
# try:
client = pymongo.MongoClient('url for the db')
db = client['stock_data']
collection = db['icici_bank']
# except:
#     print("error")
    # exit()

# Function to store stock data
def store_stock_data():
    now = datetime.datetime.now()
    start_time = datetime.datetime(now.year, now.month, now.day, 9, 15, 0)
    end_time = datetime.datetime(now.year, now.month, now.day, 14, 15, 0)
    print(start_time, end_time, now)
    if start_time <= now <= end_time:
        print("Making request......")
        ticker = yf.Ticker('ICICIBANK.NS')
        data = ticker.history(start=now, interval='15m')
        if not data.empty:
            collection.insert_many(data.reset_index().to_dict('records'))\

# Create scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(store_stock_data, 'interval', minutes=15)
scheduler.start()

# Run scheduler indefinitely
try:
    while True:
        pass
except KeyboardInterrupt:
    scheduler.shutdown()
