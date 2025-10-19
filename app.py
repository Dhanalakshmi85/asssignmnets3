from datetime import date
from flask import Flask, jsonify

# Create Flask app and set static folder for public files
app = Flask(__name__, static_folder="public", static_url_path="/public")

@app.get("/")
def hello_world():
    """Root endpoint — returns a simple message."""
    return "Hello, world! Flask is running."

@app.get("/api/v1/cat")
def get_cat():
    """Return a sample cat object in JSON."""
    cat = {
        "cat_id": "64f0c2af9c1a4b1290a0abcd",
        "name": "Misu",
        "birthdate": str(date(2022, 4, 15)),
        "weight": 4.2,
        "owner": "6500b2d39f1c4c12aa33abcd",
        "image": "https://place-hold.it/320x240&text=Cat"
    }
    return jsonify(cat)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
