
from flask import Flask, jsonify
import os
import psycopg
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/health")
def health():
    return jsonify({ "status": "healthy",
                      "app": os.getenv("APP_NAME", "Cloud App"),
                       "environment": os.getenv("ENVIRONMENT", "development")})
@app.route("/db-health")
def db_health():
    
    try:
        
        conn = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"))
            
        conn.close()
        return jsonify({"database": "connected"}), 200
    except Exception as e:
        print("DATABASE ERRORP:", e)
        return jsonify({"database": "error",
                        "message": stre(e)}), 500
@app.route("/")
def home():
    return jsonify ({ "message": "Cloud App Backend is running"})
if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5000)
