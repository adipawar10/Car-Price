import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
def app(df):
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.title("Visualised Data")
	st.subheader("Scatter Plot")
	selection=st.multiselect("Scatter Plot",["carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"])
	for i in selection:
		plt.title(f"Scatter plot for{i}")
		plt.figure(figsize=(20,10))
		plt.scatter(df[i],df["price"])
		st.pyplot()
	st.subheader("Select the plot:")
	select=st.multiselect("Plot options",["Box Plot","Histogram","Coorelation Heatmap"])
	if "Box Plot" in select:
		column=st.multiselect("Select columns for box plot:",["carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"])
		for i in column:
			plt.figure(figsize=(20,10))
			sns.boxplot(df[i])
			st.pyplot()
	if "Histogram" in select:
		column=st.multiselect("Select columns for histogram:",["carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"])
		for i in column:
		    plt.figure(figsize=(20,10))
		    sns.distplot(df[i])
		    st.pyplot()
	if "Coorelation Heatmap" in select:
		plt.figure(figsize=(20,10))
		sns.heatmap(df.corr(),annot=True)
		st.pyplot
