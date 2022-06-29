import streamlit as st
def app(df):
	st.title("Car Price Predictor")
	st.write("""This web app allows a user to predict the prices of a car based on their
	 engine size, horsepower, dimensions and the drive wheel type parameters""")
