import streamlit as st

st.set_page_config(
    page_title="Intelligent Farm Decision Assistant",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Intelligent Farm Decision Assistant")
st.subheader("Agentic AI for Agriculture")

st.write(
    "An AI-powered prototype that analyzes farm conditions "
    "and provides decision-support recommendations."
)

st.divider()

st.header("🌾 Enter Farm Information")

crop = st.selectbox(
    "Select Crop",
    ["Rice", "Wheat", "Tomato", "Cotton", "Maize"]
)

growth_stage = st.selectbox(
    "Growth Stage",
    ["Seedling", "Vegetative", "Flowering", "Maturity"]
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=60.0,
    value=30.0
)

rain_probability = st.slider(
    "Rain Probability (%)",
    0,
    100,
    30
)

soil_moisture = st.slider(
    "Soil Moisture (%)",
    0,
    100,
    50
)

disease = st.radio(
    "Are disease symptoms visible?",
    ["No", "Yes"]
)

if st.button("🤖 Analyze Farm"):

    st.header("AI Agent Analysis")

    # Weather Agent
    if rain_probability >= 60:
        weather_result = "Rain is likely. Avoid unnecessary irrigation."
    elif temperature >= 35:
        weather_result = "High temperature detected. Monitor crop water stress."
    else:
        weather_result = "Weather conditions are currently normal."

    # Soil Agent
    if soil_moisture < 30:
        soil_result = "Soil moisture is low. Irrigation may be required."
    elif soil_moisture > 80:
        soil_result = "Soil moisture is high. Avoid excessive irrigation."
    else:
        soil_result = "Soil moisture is within the monitored range."

    # Crop Agent
    crop_result = (
        f"{crop} is currently in the {growth_stage} stage. "
        "Continue monitoring crop development."
    )

    # Disease Agent
    if disease == "Yes":
        disease_result = (
            "Possible disease symptoms detected. "
            "Inspect affected plants and consult an agricultural expert."
        )
    else:
        disease_result = "No disease symptoms reported."

    st.subheader("🌦️ Weather Agent")
    st.info(weather_result)

    st.subheader("💧 Soil Agent")
    st.info(soil_result)

    st.subheader("🌱 Crop Agent")
    st.info(crop_result)

    st.subheader("🦠 Disease Agent")
    st.info(disease_result)

    st.divider()

    st.header("🌾 Final Farm Recommendation")

    if soil_moisture < 30 and rain_probability < 60:
        recommendation = (
            "Check the field and consider irrigation because "
            "soil moisture is low and significant rain is not expected."
        )
    elif rain_probability >= 60:
        recommendation = (
            "Rain is likely. Monitor the field and avoid unnecessary irrigation."
        )
    elif temperature >= 35:
        recommendation = (
            "Monitor the crop for heat stress and maintain appropriate "
            "water availability."
        )
    elif disease == "Yes":
        recommendation = (
            "Inspect affected plants and seek advice from an agricultural expert."
        )
    else:
        recommendation = (
            "Continue monitoring weather, soil moisture, crop growth, "
            "and plant health."
        )

    st.success(recommendation)

    st.caption(
        "Prototype only: recommendations should be verified with "
        "local agricultural conditions and expert advice."
    )
