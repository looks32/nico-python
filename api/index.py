from flask import Flask, render_template, request, redirect
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask("JobScrapper", template_folder=os.path.join(BASE_DIR, "..", "templates"))

db = {}

def search_jobs(keyword):
    with open(os.path.join(BASE_DIR, "..", "jobs.json"), "r", encoding="utf-8") as file:
        jobs = json.load(file)
    return [job for job in jobs if keyword.lower() in job["title"].lower()]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword not in db:
        db[keyword] = search_jobs(keyword)
    return render_template("search.html", keyword=keyword, jobs=db[keyword])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)