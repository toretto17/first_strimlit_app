import streamlit as st
import pandas as pd
import requests

st.title('Hii frineds, chai pilo')
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range Egg')
st.text('🥑🍞Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
selected_fruits = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
to_show = my_fruit_list.loc[selected_fruits]
st.dataframe(to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.header("Fruityvice Fruit Advice!")
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)

