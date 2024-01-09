import streamlit 
import pandas as pd

streamlit.title('My Patrents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal 🥣')
streamlit.text('Kale, Spinach & Rocket Smoothie 🥗')
streamlit.text('Hard-Boiled Free-Range Egg 🐔 ')
streamlit.text('Avacado Toast 🥑🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

sstreamlit.multiselect("Pick what you want",list(my_fruit_list.list),['Avacdo','Strawberry'])
