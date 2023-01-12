import requests
import streamlit as st

url = "https://8b23-86-234-101-228.eu.ngrok.io/"

st.title("Predict a car price")

col1, col2, col3 = st.columns(3)
with col1:
    enginesize = st.number_input('Choose a engine size', min_value=50, max_value=350)

with col2:
    curbweight = st.number_input('Pick a curbweight', min_value=1000, max_value=5000)

with col3:
    horsepower = st.number_input('Choose a horsepower', min_value=45, max_value=300)

url_searched = f"{url}?enginsize={enginesize}&curbweight={curbweight}&horsepower={horsepower}"
req = requests.get(url_searched).json()

st.markdown(f"### The predicted price is {req['car price prediction']}$")
