from pymongo import MongoClient
from flask import Flask
from flask import render_template
import json
from bson import json_util
from bson.json_util import dumps


app = Flask(__name__)
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DATABASE_NAME = 'bloombergdata'
COLLECTION_NAME = 'repo_data2'
FIELDS = {'Name': True, 'Size': True, 'Languages': True, 'TotalLoc': True, "_id": False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bloombergdata/repo_data2")
def github_visualisation_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DATABASE_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(debug=True)
