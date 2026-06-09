from flask import Flask, render_template, request, redirect, send_file
import json

def search_jobs(keyword):
    with open("jobs.json", "r", encoding="utf-8") as file:
        jobs = json.load(file)

    result = []

    for job in jobs:
        if keyword.lower() in job["title"].lower():
            result.append(job)

    return result

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = search_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("0.0.0.0") 