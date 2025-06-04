import streamlit as st
import pickle
import requests

# ✅ TMDB API key
API_KEY = "03936de649ce9b90e3aed43aa849862f"

# ✅ Poster fetcher with error handling
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if not poster_path:
            return "https://via.placeholder.com/500x750?text=No+Poster"
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Poster+Error"

# ✅ Load models and movie data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# ✅ Page Header
st.header("🎬 Movie Recommender System")

# ✅ Static Posters (Top Picks)
imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]

# ✅ Display carousel-style row of top posters
st.subheader("🎞️ Popular Posters")
cols = st.columns(5)
for i, url in enumerate(imageUrls[:5]):
    with cols[i]:
        st.image(url)

# ✅ Dropdown to select movie
selectvalue = st.selectbox("🎥 Select a movie to get recommendations", movies_list)

# ✅ Recommendation engine
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movies = []
    recommended_posters = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# ✅ Show recommendations when button is clicked
if st.button("Show Recommend"):
    movie_names, movie_posters = recommend(selectvalue)
    st.subheader("🎯 Recommended Movies")
    columns = st.columns(5)
    for i in range(5):
        with columns[i]:
            st.text(movie_names[i])
            st.image(movie_posters[i])
