import streamlit as st

from decision_engine import farm_decision


st.set_page_config(
    page_title="Intelligent Farm Decision Assistant",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Intelligent Farm Decision Assistant")
st.subheader("Agentic AI for Agriculture")

st.write(
    "An intelligent decision-support system that analyzes "
    "weather, soil, crop and disease information."
)

st.divider()

st.header("🌾 Farm Information")

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

disease_symptoms = st.radio(
    "Are disease symptoms visible?",
    ["No", "Yes"]
)


if st.button("🤖 Analyze Farm"):

    result = farm_decision(
        crop=crop,
        growth_stage=growth_stage,
        temperature=temperature,
        rain_probability=rain_probability,
        soil_moisture=soil_moisture,
        disease_symptoms=disease_symptoms
    )

    st.header("🤖 AI Agent Analysis")

    st.subheader("🌦️ Weather Agent")
    st.info(result["Weather Agent"])

    st.subheader("💧 Soil Agent")
    st.info(result["Soil Agent"])

    st.subheader("🌱 Crop Agent")
    st.info(result["Crop Agent"])

    st.subheader("🦠 Disease Agent")
    st.info(result["Disease Agent"])

    st.subheader("💰 Market Agent")
    st.info(result["Market Agent"])

    st.divider()

    st.header("🧠 Final Decision")

    for recommendation in result["Recommendations"]:
        st.success(recommendation)

    st.caption(
        "This is a prototype decision-support system. "
        "Verify recommendations with local agricultural conditions "
        "and qualified agricultural experts."
    )
