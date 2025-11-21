# Code run in Pymongo
#Connects MySQL with Python MySQL driver

import mysql.connector
from pymongo import MongoClient

# Connect to MySQL
conn = mysql.connector.connect(
    user="root",
    password="PASSWORD",   # MySQL password
    host="localhost",
    database="SanFranSortedDatabase"
)
cursor = conn.cursor(dictionary=True)

# Connect to MongoDB Atlas # Stringcopypasted from MongoDB Atlas.
client = MongoClient("mongodb+srv://Allankpvang:”PASSWORD”@assignment2.rttjxxl.mongodb.net/?retryWrites=true&w=majority")
db = client["SanFranSortedDatabase"]

# Function to transfer only the first 10,000 rows
def transfer_table(table_name, collection_name):
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 10000")
    rows = cursor.fetchall()
    
    if rows:
        db[collection_name].insert_many(rows)
        print(f"Inserted {len(rows)} rows into {collection_name}")

# Transfer each table (first 10k rows only)
transfer_table("patron", "patron") 
transfer_table("home_library", "home_library")
transfer_table("circulation_activity", "circulation_activity")
transfer_table("notification_preferences", "notification_preferences")

#This lets me know that Python is done importing my code
print(" Imported first 10,000 rows into MongoDB Atlas.")
