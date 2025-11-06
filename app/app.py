from flask import Flask, render_template
from db_config import get_connection

app = Flask(__name__)

@app.route("/")
def index():
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM patron;")
  results = cursor.fetchall()
  cursor.close()
  conn.close()
  return render_template("index.html", data=results)

if __name__ == "__main__":
  app.run(debug=True)
