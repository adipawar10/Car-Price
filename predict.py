import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_squared_log_error
def app(df):
	st.markdown("<p style='color:pink;font-size:40px'>Welcome to the <b>Car Prediction App</b>!</p>",unsafe_allow_html=True)
	carw=st.slider("CarWidth",float(df["carwidth"].min()),float(df["carwidth"].max()))
	engs=st.slider("EngineSize",float(df["enginesize"].min()),float(df["enginesize"].max()))
	horp=st.slider("Horsepower",float(df["horsepower"].min()),float(df["horsepower"].max()))
	comb=st.radio("Is the car manufactured by buick?",[0,1])
	dfwd=st.radio("Is it a front wheel drive car?",[0,1])
	#if comb=="No":
		#comb=0
    #else:
       # comb=1
    
    #if dfwd==No:
        #dfwd=0
    #else:
        #dfwd=1
	if st.button("Predict"):
	    st.header("Prediction Result")
	    pred1,r2,mse, rmse, mae,msle,score=prediction(carw,engs,horp,comb,dfwd,df)
	    st.success(f"The predicted price of the car is:{pred1[0]:.2f}$")
	    st.info(f"The accuracy is:{score}")
	    st.info(f"The r2_score is:{r2}")
	    st.info(f"The mean squared error is:{mse}")
	    st.info(f"The root mean squared error is:{rmse}")
	    st.info(f"The mean squared log error is:{msle}")
	    st.info(f"The  mean_absolute_error is:{mae}")



def prediction(carw,engs,horp,comb,dfwd,df):
	target=df["price"]
	feature=df[df.columns[:-1]]
	x_train,x_test,y_train,y_test=train_test_split(feature,target,random_state=42,test_size=0.3)
	obj=LinearRegression()
	obj.fit(x_train,y_train)
	score=obj.score(x_train,y_train)
	pred1=obj.predict([[carw,engs,horp,comb,dfwd]])
	pred=obj.predict(x_test)
	r2=r2_score(y_test,pred)
	mse=mean_squared_error(y_test,pred)
	rmse=np.sqrt(mse)
	mae=mean_absolute_error(y_test,pred)
	msle=mean_squared_log_error(y_test,pred)
	return pred1,r2,mse, rmse, mae,msle,score



