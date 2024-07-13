import requests
import streamlit as st
import pickle
import pandas as pd
import os
import base64

st.set_page_config(layout="wide")
# Custom CSS to inject into the Streamlit app
st.markdown("""
<style>
.navbar {
    background-color: black;
    padding: 12px;
    width: 1412px;
    float: left;
    text-align: left;
    margin-top: 0px;
    
}
.nav-button {
    display: inline;
    font-size: 16px;
    color: white;
    text-align: center;
    width: 100px;
    font-weight: bold;
    margin-left: 150px;
    background-color: black;
    opacity: 05;
}
.nav-button:hover {
background-color: white;
}
.nav-button:focus {
background-color: red;
}
</style>
""", unsafe_allow_html=True)

# Navbar layout
st.markdown("""
<div class="navbar">
    <button class="nav-button" onclick="window.location.href = '#';" autofocus >Home</button>
    <button class="nav-button" onclick="window.location.href = 'index.html';">Login</button>
</div>
""", unsafe_allow_html=True)


# Autoclick the Home button using JavaScript
st.markdown("""
<script>
document.getElementsByClassName('nav-button')[0].click();
</script>
""", unsafe_allow_html=True)




@st.cache_data
def get_img(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

local_image_path = 'wallpaper.jpg'  # make sure the image is in the same folder
img = get_img(local_image_path)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
def fatch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[0:10]

    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from Api
        recommend_movies_posters.append(fatch_poster(movie_id))
    return recommend_movies, recommend_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name: object = st.selectbox('',
                                            movies['title'].values)
j = 1
if st.button('Search Movie'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col2, col3 , col3, col2, col3= st.columns(8)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    st.header("Recomendded movies")
    col1, col2, col3, col4, col5, col6, col7, col8 , col9= st.columns(9)

    with col1:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        with col2:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
            with col3:
                st.text(recommended_movie_names[3])
                st.image(recommended_movie_posters[3])
                with col4:
                    st.text(recommended_movie_names[4])
                    st.image(recommended_movie_posters[4])
                    with col5:
                        st.text(recommended_movie_names[5])
                        st.image(recommended_movie_posters[5])
                        with col6:
                            st.text(recommended_movie_names[6])
                            st.image(recommended_movie_posters[6])
                            with col7:
                                st.text(recommended_movie_names[7])
                                st.image(recommended_movie_posters[7])
                                with col8:
                                    st.text(recommended_movie_names[8])
                                    st.image(recommended_movie_posters[8])
                                    with col9:
                                        st.text(recommended_movie_names[9])
                                        st.image(recommended_movie_posters[9])




