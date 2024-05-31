import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(layout='wide', page_title='Alpha Movies', page_icon='🎬', initial_sidebar_state="collapsed")

if 'cart' not in st.session_state:
    st.session_state.cart = []
mv = []

def main():

    st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
    st.title("Alpha Movies")

    # Loading data from the csv to python
    movie = pd.read_csv('movies_cleaned_dataset.csv')

    # Sidebar which has search attributes options
    st.sidebar.title("Welcome to Alpha Movies")
    Movies = st.sidebar.text_input("Enter Movie Title:")
    Released_Year = st.sidebar.text_input("Enter Released Year:")
    Genre = st.sidebar.selectbox("Select Genre:", [""] + list(movie['Genre'].unique()))
    search_button = st.sidebar.button("Search")

    # Movies Display Structure 
    num_cols = 4  # Number of columns for the grid structure
    num_movies = len(movie)
    num_rows = (num_movies + num_cols - 1) // num_cols  # Calculation for the number of rows

    # Create columns for the grid
    cols = st.columns(num_cols)

    # Display movie details in the grid form where they are displayed in rows and colunms
    idx = 0
    while idx < num_movies:
        for row in range(num_rows):
            for col in range(num_cols):
                if idx < num_movies:
                    if filter_movie(movie.iloc[idx], Movies, Released_Year, Genre):
                        with cols[col]:
                            # Movie poster and title
                            st.image(movie["Poster_Link"][idx], width=120)
                            st.markdown(f"<h3 style='font-size: 18px;'>{movie['Movies'][idx]}</h3>", unsafe_allow_html=True)
                            if st.button(f"View", key=f"view_btn_{idx}"):  # Use unique key based on movie title and index
                                # st.session_state.cart.append(movie.iloc[idx])
                                mv.append(movie.iloc[idx])
                                show_movie_details(movie.iloc[idx], mv)  # Pass session_state to update cart
                    idx += 1

def filter_movie(movie_details, title, year, genre):
    # Filter movie based on search criteria
    if title and title.lower() not in movie_details['Movies'].lower():
        return False
    if year and str(movie_details['Released_Year']) != year:
        return False
    if genre and genre != movie_details['Genre']:
        return False
    return True

def show_movie_details(movie_details, mv):
    # Display movie details for the overview of the movie
    st.subheader("Selected Movie Information")
    st.write(f"Movies: {movie_details['Movies']}")
    st.write(f"Genre: {movie_details['Genre']}")
    st.write(f"Rating: {movie_details['Rating']}")
    st.write(f"Director: {movie_details['Director']}")
    st.write(f"Released_Year: {movie_details['Released_Year']}")
    st.write(f"Overview: {movie_details['Overview']}")
    st.write(f"Runtime: {movie_details['Runtime']}")
    st.write(f"Star1: {movie_details['Star1']}")
    st.write(f"Star2: {movie_details['Star2']}")
    st.write(f"Star3: {movie_details['Star3']}")
    st.write(f"Star4: {movie_details['Star4']}")
    st.write(f"Prices: {movie_details['Prices']}")
    st.page_link("/Users/da-m1-18/Downloads/payment.py", label=" Checkout", icon="2️⃣")
    
   #CART MOVIE OPTION FOR ADD AND DISPLAY 
    
    # Button that adds/cancel movie cart
    if st.button("cancel cart", key=f"add_to_cart_{movie_details['Movies']}"):
        # session_state.cart = movie_details
        st.header("Your Cart:")
        st.write(mv)

    # Display Cart on the side bar after selecting
    st.sidebar.header("Your Cart:")
    st.sidebar.write(movie_details['Movies'])


if __name__ == "__main__":
    main()






