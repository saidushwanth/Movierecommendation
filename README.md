# 🎬 Movie Recommendation System
website link:https://movierecommendation-smcg6rmxf7qwc9zmeakmc2.streamlit.app/
A content-based movie recommendation system built using Python, Pandas, and Scikit-learn. This project suggests similar movies based on the content and features of a given movie title using natural language processing techniques.

## 📌 Features

- Recommends movies based on similarity of:
  - Genres
  - Cast
  - Crew
  - Keywords
- Uses TF-IDF and CountVectorizer for feature extraction
- Cosine similarity used for finding similar movies
- Simple and interactive console interface

## 📂 Dataset

The system is trained on the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), which includes:
- 5000+ movies
- Metadata like genres, cast, crew, keywords, and overview

## ⚙️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- NLTK (optional for advanced NLP)
- Jupyter Notebook (for development)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/saidushwanth/Movierecommendation.git
cd Movierecommendation
2. Install Dependencies
Make sure you have Python installed. Then run:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not available, manually install:

bash
Copy
Edit
pip install pandas scikit-learn numpy
3. Run the Code
Open the Jupyter Notebook:

bash
Copy
Edit
jupyter notebook main.ipynb
Or run the Python file directly (if provided):

bash
Copy
Edit
python app.py
4. Example Output
Input:

css
Copy
Edit
Enter a movie: Avatar
Output:

markdown
Copy
Edit
Top 5 similar movies:
1. John Carter
2. Guardians of the Galaxy
3. Prometheus
4. Battleship
5. The Avenger
