import streamlit

streamlit.title ('My parents New Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega & Blueberry Smoothie')
streamlit.text('🥗 Kale, spinach & rocky smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#pick a fruit
streamlit.multiselect("Pick some fruits:"list(my_fruit_list.indx))
streamlit.dataframe(my_fruit_list)
