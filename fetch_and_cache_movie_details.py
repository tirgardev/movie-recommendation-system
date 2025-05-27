import pickle
import pandas as pd
import requests
import time

# Load your movies list
movies = pickle.load(open('movies.pkl', 'rb'))

# OMDb API Key
OMDB_API_KEY = 'a8ef895b'  # Replace with your actual API key

movie_details = []

for idx, title in enumerate(movies['title']):
    print(f"Fetching {idx+1}/{len(movies)}: {title}")
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
        response = requests.get(url)
        data = response.json()

        poster = data.get('Poster', "https://via.placeholder.com/500x750.png?text=No+Image")
        if poster == 'N/A':
            poster = "https://via.placeholder.com/500x750.png?text=No+Image"

        rating = data.get('imdbRating', 'N/A')
        genre = data.get('Genre', 'N/A')
        plot = data.get('Plot', 'N/A')
        year = data.get('Year', 'N/A')

        movie_details.append({
            "title": title,
            "poster": poster,
            "rating": rating,
            "genre": genre,
            "plot": plot,
            "year": year
        })
    except Exception as e:
        print(f"Error fetching {title}: {e}")
        movie_details.append({
            "title": title,
            "poster": "https://via.placeholder.com/500x750.png?text=Error",
            "rating": "N/A",
            "genre": "N/A",
            "plot": "N/A",
            "year": "N/A"
        })
    time.sleep(0.3)  # Sleep to avoid hitting API rate limits

# Save the details locally
details_df = pd.DataFrame(movie_details)
details_df.to_pickle('movie_details_cache.pkl')
print("Movie details cached successfully!")
