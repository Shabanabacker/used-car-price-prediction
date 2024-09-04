import streamlit as st
import joblib
import pandas as pd

# Load the trained model and scaler
model = joblib.load("random_forest_model.joblib")
scaler = joblib.load("scaler.joblib")
label_encoders = joblib.load("label_encoders.joblib")

# Define numerical and categorical columns
numerical_cols = [
    'Kilometers_driven', 'No_of_previous_owners', 'Year_of_car_manufacture',
    'Seats', 'Engine Displacement in cc', 'Mileage in kmpl', 
    'Max Power in bhp', 'Torque in Nm', 'Top Speed in kmph', 'Age_of_Car'
]

categorical_cols = [
    'City', 'Fuel_type', 'Body_type', 'Transmission_type',
    'Original_Equipment_Manufacturer', 'Car_model', 
    'Variant_name', 'Color', 'Drive Type'
]

# Input fields for numerical features
st.header("Used Car Price Prediction")
Kilometers_driven = st.slider("Kilometers driven",  min_value=0, max_value=1000000, step=100)
No_of_previous_owners = st.number_input("Number of previous owners", min_value=0, max_value=10)
Year_of_car_manufacture = st.number_input("Year of car manufacture", min_value=1980, max_value=2024)
Seats = st.number_input("Number of seats", min_value=2, max_value=8)
Engine_Displacement = st.number_input("Engine Displacement in cc", min_value=500, max_value=10000)
Mileage = st.number_input("Mileage in kmpl", min_value=0, max_value=100)
Max_Power = st.number_input("Max Power in bhp", min_value=20.0, max_value=1000.0)
Torque = st.number_input("Torque in Nm", min_value=50.0, max_value=1000.0)
Top_Speed = st.number_input("Top Speed in kmph", min_value=50, max_value=400)
Age_of_Car = st.number_input("Age of Car", min_value=0, max_value=50)

# Input fields for categorical features
City = st.selectbox("City", label_encoders['City'].classes_)
Fuel_type = st.selectbox("Fuel type", label_encoders['Fuel_type'].classes_)
Body_type = st.selectbox("Body type", label_encoders['Body_type'].classes_)
Transmission_type = st.selectbox("Transmission type", label_encoders['Transmission_type'].classes_)
OEM = st.selectbox("Original Equipment Manufacturer", label_encoders['Original_Equipment_Manufacturer'].classes_)
Car_model = st.selectbox("Car model", label_encoders['Car_model'].classes_)
Variant_name = st.selectbox("Variant name", label_encoders['Variant_name'].classes_)
Color = st.selectbox("Color", label_encoders['Color'].classes_)
Drive_Type = st.selectbox("Drive Type", label_encoders['Drive Type'].classes_)

# Create a DataFrame for input
input_data = pd.DataFrame({'City': [City],
                           'Fuel_type': [Fuel_type],
    'Body_type': [Body_type],
    'Kilometers_driven': [Kilometers_driven],
    'Transmission_type': [Transmission_type],
    'No_of_previous_owners': [No_of_previous_owners],
    'Original_Equipment_Manufacturer': [OEM],
    'Car_model': [Car_model],
    'Year_of_car_manufacture': [Year_of_car_manufacture],
     'Variant_name': [Variant_name],
    'Seats': [Seats],
    'Color': [Color],
    'Drive Type': [Drive_Type],
    'Engine Displacement in cc': [Engine_Displacement],
    'Mileage in kmpl': [Mileage],
    'Max Power in bhp': [Max_Power],
    'Torque in Nm': [Torque],
    'Top Speed in kmph': [Top_Speed],
    'Age_of_Car': [Age_of_Car]  
})

# Reorder columns to match the order in training data
#input_data = input_data[numerical_cols + categorical_cols]

# Scale numerical features
input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])

# Encode categorical features
for col in categorical_cols:
    input_data[col] = label_encoders[col].transform(input_data[col])

# Predict the price
if st.button("Predict Price"):
    predicted_price = model.predict(input_data)
    st.success(f"The predicted price of the used car is: ₹{predicted_price[0]:,.2f}")