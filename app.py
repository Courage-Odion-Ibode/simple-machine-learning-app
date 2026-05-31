import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="centered")

# API_URL = st.secrets.get("API_URL", "http://localhost:8000/predict")
API_URL = "http://localhost:8000/predict"

st.title("House Price Prediction")
st.write("Enter the area of the house in square feet to get a price prediction.")
area_sqft = st.number_input("Area (sqft)", min_value=0.0, step=0.1)
if st.button("Predict"):
    if area_sqft > 0:
        import requests
        response = requests.post(API_URL, json={"area_sqft": area_sqft})
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Predicted Price: ${prediction:.2f}")
        else:
            st.error("Error in prediction. Please try again.")
    else:
        st.warning("Please enter a valid area in square feet.")