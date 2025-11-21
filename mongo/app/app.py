from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://Allankpvang:Mimikyu49@assignment2.rttjxxl.mongodb.net/?retryWrites=true&w=majority")
db = client["SanFranSortedDatabase"]

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = {}
    selected_collection = "patron"  # default collection

    if request.method == "POST":
      
        # Get form inputs
        selected_collection = request.form.get("collection")
        field = request.form.get("field")
        value = request.form.get("value")

        # Build MongoDB query if field/value provided
        if field and value:
            query = {field: {"$regex": value, "$options": "i"}}  # case-insensitive search

    # Run query on chosen collection, All 10,000 rows
    results = list(db[selected_collection].find(query).limit(10000))

    return render_template("index.html", data=results, collection=selected_collection)

if __name__ == "__main__":
    app.run(debug=True)
