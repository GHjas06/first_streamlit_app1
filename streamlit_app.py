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
my_fruit_list=my_fruit_list.set_index('Fruit')
#pick a fruit
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

import requests

fruit_choice = streamlit.text_input('What fruit would you like to explore?','kiwi')
streamlit.write ('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())

# normalize the json data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# tabular form
streamlit.dataframe(fruityvice_normalized)
