import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load('xgboost_model.pkl')

st.set_page_config(page_title="CA Home Price Estimator", layout="centered")
st.title("🏡 California Home Price Predictor")
st.write("Enter the details of the house below:")

# User inputs
# living_area = st.number_input("Living Area (sq ft)", min_value=200, max_value=10000, value=1500)
# bedrooms = st.slider("Number of Bedrooms", 1, 10, value=3)
# bathrooms = st.slider("Number of Bathrooms", 1, 10, value=2)
# garage = st.selectbox("Garage", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
# zipcode = st.number_input("Zip Code", min_value=90001, max_value=96162, value=94107)
# latitude = st.number_input("Latitude", value=37.77)
# longitude = st.number_input("Longitude", value=-122.42)


# ViewYN	PoolPrivateYN	LivingArea	CountyOrParish	PropertySubType	PropertyType	LotSizeSquareFeet	YearBuilt	BathroomsTotalInteger	BedroomsTotal	GarageSpaces	ClosePrice	NewConstructionYN	Levels	ParkingTotal	FireplaceYN	City	Latitude	Longitude
ViewYN = st.selectbox("Does the property have a visually appealing view (Ex. Ocean, Park, Skyline, Forest, Mountain)", options = [0,1], format_func = lambda x: "Yes" if x else "No")
PoolPrivateYN = st.selectbox("Does the property have a private pool", options = [0,1], format_func = lambda x: "Yes" if x else "No")
NewConstructionYN = st.selectbox("Is this house a new construction, (Within a year of being built)", options = [0,1],format_func = lambda x: "Yes" if x else "No")
FirePlaceYN = st.selectbox("Does this house have a fireplace", options = [0,1], format_func= lambda x: "Yes" if x else "No")

LivingArea = st.number_input("How much sqft does the living area of your property have", min_value=0.0, max_value=15024.0, value=0.0)
LotSizeSquareFeet = st.number_input("How much sqft does the entire property have (outdoor and indoor)", min_value=0.0, max_value=851143600.0, value=0.0)
YearBuilt = st.number_input("What year was the house built", min_value=1868.0, max_value=2025.0, value=2020.0)
BathroomsTotalInteger = st.number_input("How many total bathrooms does your property have", min_value=0.0, max_value=14.0, value=1.0)
BedroomsTotal = st.number_input("How many bedrooms does your property have",min_value=0.0, max_value=14.0, value=1.0)
GarageSpaces = st.number_input("How many total cars can fit in your garage", min_value=0.0, max_value=23.0, value=1.0)
ParkingTotal = st.number_input("Total number of parking spaces on your property",min_value=0.0, max_value=76.0, value=1.0 )
Latitude = st.number_input("Latitude (rounded to nearest hundredth)", min_value=31.51, max_value=40.035, value=round(32.77, 2), step=0.01, format="%.2f")
Longitude = st.number_input("Longitude (rounded to nearest hundredth)", min_value=-123.01, max_value=-114.31, value=round(-122.42, 2), step=0.01, format="%.2f")

CountyOrParish = st.selectbox(
    "Select your city",
    options=[
        "Los Angeles", "Orange", "Riverside", "San Bernardino", "San Diego",
        "San Luis Obispo", "Ventura", "Butte", "Contra Costa", "Kern",
        "Alameda", "Merced", "Lake", "Santa Barbara", "Fresno", "Madera",
        "Tehama", "Glenn", "Stanislaus", "Mariposa", "Tulare", "Santa Clara",
        "Imperial", "Kings", "Solano", "Yuba"
    ]
)
PropertySubType = st.selectbox(
    "SingleFamilyResidence",
    options = ["SingleFamilyResidence"]
)
PropertyType = st.selectbox(
    "Residential",
    options = ["Residential"]
)
Levels = st.selectbox(
    "How many Levels does your property have?",
    options = ["One" ,"Two","ThreeOrMore", "MultiSplit"]
)


# # Optional: Interaction term (example)
# area_times_bed = living_area * bedrooms

# Create DataFrame for prediction
input_data = pd.DataFrame({
    'ViewYN': [ViewYN],
    'PoolPrivateYN': [PoolPrivateYN],
    'NewConstructionYN': [NewConstructionYN],
    'FireplaceYN': [FirePlaceYN],
    'LivingArea': [LivingArea],
    'LotSizeSquareFeet': [LotSizeSquareFeet],
    'YearBuilt': [YearBuilt],
    'BathroomsTotalInteger': [BathroomsTotalInteger],
    'BedroomsTotal': [BedroomsTotal],
    'GarageSpaces': [GarageSpaces],
    'ParkingTotal': [ParkingTotal],
    'Latitude': [round(Latitude, 2)],
    'Longitude': [round(Longitude, 2)],
    'CountyOrParish': [CountyOrParish],
    'PropertySubType': [PropertySubType],
    'PropertyType': [PropertyType],
    'Levels': [Levels]
})

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Sale Price: ${prediction[0]:,.0f}")