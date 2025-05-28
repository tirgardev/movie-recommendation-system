import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_details = pd.read_pickle('movie_details_cache.pkl')

# Fetch from cache
def fetch_movie_details_from_cache(movie_title):
    detail = movie_details[movie_details['title'] == movie_title]
    if not detail.empty:
        row = detail.iloc[0]
        return row['poster'], row['rating'], row['genre'], row['plot'], row['year']
    else:
        return "https://via.placeholder.com/500x750.png?text=No+Image", "N/A", "N/A", "N/A", "N/A"

# Recommendation logic
def recommend_all(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    
    recommendations = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        poster, rating, genre, plot, year = fetch_movie_details_from_cache(title)
        recommendations.append({
            "title": title,
            "poster": poster,
            "rating": rating,
            "genre": genre,
            "plot": plot,
            "year": year
        })
    return recommendations

# 🎨 UI Settings
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎥 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.write("Get content-based movie suggestions powered by Machine Learning and cached OMDb data.")

selected_movie_name = st.selectbox("🎞️ Select a movie:", movies['title'].values)

if st.button("🔍 Show Recommendations"):
    recommendations = recommend_all(selected_movie_name)
    st.markdown("### 📌 Top 10 Similar Movies:")

    for rec in recommendations:
        with st.container():
            cols = st.columns([1, 2])
            with cols[0]:
                st.image(rec["poster"], use_container_width=True)
            with cols[1]:
                st.markdown(f"#### 🎬 {rec['title']} ({rec['year']})")
                st.markdown(f"**⭐ IMDb Rating:** {rec['rating']}")
                st.markdown(f"**🎭 Genre:** {rec['genre']}")
                st.markdown(f"**🧾 Plot:** {rec['plot']}")
                st.markdown("---")

