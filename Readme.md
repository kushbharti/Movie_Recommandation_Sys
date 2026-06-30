# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Machine Learning, Natural Language Processing (NLP), and Streamlit. The application recommends similar movies based on movie metadata such as genres, keywords, cast members, directors, and movie overviews.

---

## 📖 Description

Finding a good movie to watch can be difficult when thousands of options are available. This project helps users discover movies similar to their favorite ones using a content-based recommendation approach.

The system analyzes movie information including genres, keywords, cast, directors, and plot descriptions to calculate similarities between movies. When a user selects a movie, the system recommends the most relevant movies along with their posters fetched dynamically from The Movie Database (TMDB) API.

This project demonstrates practical applications of Machine Learning, Natural Language Processing (NLP), and Recommendation Systems.

---

## 🚀 Features

- 🎥 Content-Based Movie Recommendation System
- 🔍 Search and select movies from a dropdown list
- 🧠 TF-IDF based feature extraction
- 📊 Cosine Similarity recommendation engine
- ✂️ Text preprocessing using NLTK Stemming
- 🎭 Uses genres, keywords, cast, directors, and overview
- 🖼️ Dynamic movie poster fetching using TMDB API
- ⚡ Interactive Streamlit user interface
- 🔐 Secure API key management using Environment Variables
- 📦 Preprocessed movie data stored using Pickle

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Machine Learning & NLP

- Scikit-Learn
- NLTK

### Data Processing

- Pandas
- NumPy

### API Integration

- TMDB API
- Requests

### Environment Management

- Python Decouple

### Model Storage

- Pickle

---

## 📂 Project Structure

```bash
Movie-Recommendation-System/
│
├── app.py
├── model_train.py
├── utils.py
│
├── movies_dict.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
│
├── .env
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git

cd movie-recommendation-system
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment Variables

Create a `.env` file in the project root directory.

```env
API_KEY=YOUR_TMDB_API_KEY
```

### 5. Get TMDB API Key

1. Create an account on TMDB.
2. Generate an API Key.
3. Add the API key to the `.env` file.

### 6. Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Recommendation Results

<img width="1737" height="928" alt="Screenshot 2026-06-17 112157" src="https://github.com/user-attachments/assets/026a13d5-b692-4bb4-a364-6245a91db1c4" />

<img width="1597" height="925" alt="Screenshot 2026-06-17 112348" src="https://github.com/user-attachments/assets/adb8d3c5-79dc-4f5f-9d2b-896fcc8142bf" />

---

## ▶️ Usage

1. Launch the Streamlit application.
2. Select a movie from the dropdown list.
3. Click the **Search Movie** button.
4. The system computes similarity scores.
5. Top recommended movies are displayed.
6. Posters are fetched dynamically from TMDB.

---

## 🧠 Recommendation Algorithm

This project uses a **Content-Based Filtering** approach.

### Workflow

1. Load Movie and Credits datasets.
2. Merge datasets using movie title.
3. Extract:
   - Genres
   - Keywords
   - Cast
   - Directors
   - Overview
4. Create combined tags.
5. Apply text preprocessing.
6. Perform stemming using NLTK Porter Stemmer.
7. Convert text into vectors using TF-IDF.
8. Calculate Cosine Similarity.
9. Recommend Top 5 similar movies.

