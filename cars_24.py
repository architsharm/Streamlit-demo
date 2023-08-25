import streamlit as st
import pandas as pd 
import pickle
cars_df = pd.read_csv("./cars24-car-price.csv")
st.write("""
     # Cars24 Used Car Price Prediction
    """)

fuels = st.selectbox('Fuel Type',["Diesel", "Petrol", "CNG", "LPG", "Electric"])
transmission_type = st.selectbox('Transmission Type',["Manual", "Automatic"])
seats = st.selectbox('Seat Count',[4,5,7,9,11])
engine=st.slider('Engine', 0, 2500, 100)
# Load the model
with open("car_pred", 'rb') as file:
    reg_model = pickle.load(file)
## Convert the user inputs to actual model inputs
# Replace NUll with a value
# Encode
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}
# normalisation
def model_predict(fuels,transmission_type,engine,seats):
    input_features = [[2018.0, 1, 4000, encode_dict["fuel_type"][fuels], encode_dict["transmission_type"][transmission_type],19.70, engine, 86.30, seats]]
    return reg_model.predict(input_features)

if st.button('Predict Price'):
    price=model_predict(fuels,transmission_type,engine,seats)
    st.text("Predicted Price of the car is: "+str(price))





