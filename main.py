# Adam Alberski
# 11/2/2025     

import os
import pandas as pd
import random
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

API_KEY = os.getenv("TMDB_API_KEY")

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    pair = random.sample(movies, 2)
    winner = None

    if request.method == "POST":
        winner = request.form["winner"]
    
    poster = get_poster(winner)

    return render_template("index.html", pair=pair, winner=winner, poster=poster)

df = pd.read_csv("watched.csv")
movies = df["Name"].dropna().tolist()

# Get the poser for a movie given its title
def get_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(url)
    data = response.json()
    poster_path = data["results"][0]["poster_path"]
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return poster_url

if __name__ == '__main__':
    app.run(debug=True)
    