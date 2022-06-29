import streamlit as st
import pandas as pd
def app(df):
	st.title("View Data:")
	with st.expander("Dataset"):
		st.table(df)
	st.title("Data Description:")
	if st.checkbox("Show Summary:"):
		st.table(df.describe())
	#if st.checkbox("Show Column Data:"):
	    #var=st.selectbox("Columns",["carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"])
        #st.write(df[var])
	col1,col2=st.columns(2)
	with col1:
		if st.checkbox("Column Names:"):
			st.table(df.columns)
	with col2:
		if st.checkbox("Column Datatype:"):
		    st.write(list(df.dtypes))


		    


