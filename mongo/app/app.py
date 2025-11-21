from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://Allankpvang:Mimikyu49!@assignment2.rttjxxl.mongodb.net/?retryWrites=true&w=majority")
db = client["SanFranSortedDatabase"]

@app.route("/")
def index():
  
    # Fetch first 100 rows from patron collection for display
    patrons = list(db.patron.find().limit(100))
    return render_template("index.html", data=patrons)

if __name__ == "__main__":
    app.run(debug=True)
