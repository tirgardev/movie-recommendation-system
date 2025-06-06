---
````markdown
# 🎬 Movie Recommendation System 🎥

This project is a **Content-Based Movie Recommendation System** built using **Python**, **Streamlit**, and **Machine Learning**. The system suggests movies based on a given movie title by computing the similarity score between movies using their content features.

---

## 📌 Features

- 🔍 Recommend movies similar to a selected movie
- 🧠 Content-based filtering using cosine similarity
- 🎯 Uses pre-processed movie metadata
- 💾 Pickle files for faster loading and performance
- 📺 Poster and info fetched via OMDb API
- 🌐 Deployed as a simple and interactive Streamlit web app

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn** for cosine similarity
- **Pickle** for model/data serialization
- **Streamlit** for web interface
- **OMDb API** for fetching movie posters and details
- **Google Colab / Jupyter Notebook** for initial data exploration and model training

---

## 📂 Project Structure

```bash
movie-recommendation-system/
│
├── app.py                   # Streamlit main app
├── recommendation.py        # Movie recommendation logic
├── fetch_poster.py          # Fetches movie posters using OMDb API
├── movies.pkl               # Pickled movies data
├── similarity.pkl           # Pickled similarity matrix
├── requirements.txt         # Required Python libraries
├── README.md                # Project documentation
└── dataset/                 # (Optional) Raw dataset used for training
````

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/tirgardev/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate.bat    # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Place your `.pkl` files

Ensure `movies.pkl` and `similarity.pkl` are placed in the root directory. These contain the movie metadata and similarity scores.

> 🔐 If you want to create them yourself from a dataset like TMDB/IMDb:
>
> * Use `TfidfVectorizer` or `CountVectorizer`
> * Compute cosine similarity matrix
> * Save using `pickle.dump()`

### 5. Add your OMDb API Key

In `fetch_poster.py` or directly in `app.py`, replace with your OMDb API key:

```python
OMDB_API_KEY = 'your_api_key_here'
```

> Get a free API key at: [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

---

## 🚀 Run the Streamlit App

```bash
streamlit run app.py
```

This will open a browser window where you can interact with the movie recommendation system.

---

## 🧠 How It Works

1. User selects a movie from the dropdown
2. The system finds the index of the movie in the dataset
3. It fetches similarity scores from `similarity.pkl`
4. Returns the top 5 most similar movies
5. Fetches posters and additional info from OMDb API
6. Displays all in a user-friendly web app

---

## 🗃️ Dataset Information

You can use a dataset like [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) or any metadata-rich dataset. Preprocessing typically involves:

* Combining genres, keywords, overview, etc. into one column
* Converting text to vectors using TF-IDF or CountVectorizer
* Computing cosine similarity

---

## 🧑‍💻 Authors

* 🔸 **Dev Tirgar** – [GitHub](https://github.com/tirgardev)
* 🤝 **Amit Rathod** – [GitHub](https://github.com/Amit-Rathod03)

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🌟 Show Your Support

If you like this project:

* ⭐ Star this repository
* 🖊️ Give feedback or suggestions
* 🧑‍💼 Share your own improvements or fork

---

## 📷 Preview

![Streamlit UI Preview](https://user-images.githubusercontent.com/your-screenshot-url)

---

```
