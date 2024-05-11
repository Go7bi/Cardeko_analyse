import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
with open('RandomForest_model.pkl', 'rb') as file:
    model = pickle.load(file)
def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background: url("https://images.pexels.com/photos/168938/pexels-photo-168938.jpeg");
                        background-size: cover}}
                     </style>""",unsafe_allow_html=True) 
setting_bg()
def main():
    st.title(':green[Car Price Prediction App]')
    st.sidebar.header('Input Features')
    engine_displacement = st.sidebar.slider('Engine Displacement(cc)', 75, 5000, 2000)
    year_of_manufacture = st.sidebar.slider('Year of Manufacture', 2000, 2023, 2010)
    kms_driven = st.sidebar.slider('Kms Driven(kms)', 0, 200000, 50000)
    top_speed = st.sidebar.slider('Top Speed(kmph)', 50, 300, 150)
    mileage = st.sidebar.slider('Mileage(kmpl)', 5, 30, 15)

    input_data = pd.DataFrame({
    'Engine Displacement(cc)': [engine_displacement],
    'Year of Manufacture': [year_of_manufacture],
    'Kms Driven(kms)': [kms_driven],
    'Top Speed(kmph)': [top_speed],
    'Mileage(kmpl)': [mileage]
    })

    prediction = model.predict(input_data)[0]

    st.header(':orange[Car Price Prediction]:')
    st.subheader(f':red[The predicted price for the car is: ₹{prediction:,.2f}]')
    

if __name__ == '__main__':
    main()
