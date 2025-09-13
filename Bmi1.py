import streamlit as st
import time

# Function to calculate BMI
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Function to return category and message based on BMI
def get_bmi_feedback(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️ You are below the healthy range. Consider consulting a nutritionist."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "✅ Great! You are within the healthy BMI range."
    elif 25 <= bmi < 29.9:
        return "Overweight", "📈 You are above the normal range. A balanced diet and exercise may help."
    else:
        return "Obese", "🚨 You are in the obese category. Please consult a healthcare provider."

# Page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

# Title and intro
st.markdown("""
    <h1 style='text-align: center;'>🧮 BMI Calculator</h1>
    <p style='text-align: center;'>Easily calculate your Body Mass Index (BMI) and understand your health status 💪</p>
    <hr>
""", unsafe_allow_html=True)

# Input section
st.subheader("📌 Enter Your Details")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("⚖️ Weight (in kilograms)", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("📏 Height (in centimeters)", min_value=30.0, format="%.2f")

# Calculate BMI button
if st.button("🚀 Calculate My BMI"):
    with st.spinner("Calculating..."):
        time.sleep(1)
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            category, message = get_bmi_feedback(bmi)

            # Stylish result box
            st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
                    <h2 style="color:#4CAF50;">Your BMI: {bmi}</h2>
                    <h3 style="color:#FF5733;">Category: {category}</h3>
                    <p style="font-size: 18px;">{message}</p>
                </div>
            """, unsafe_allow_html=True)

        else:
            st.error("❗ Please enter valid positive values for weight and height.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🧠 Stay healthy. Stay fit. Powered by Streamlit 💙</p>", unsafe_allow_html=True)
