from agents import (
    weather_agent,
    soil_agent,
    crop_agent,
    disease_agent,
    market_agent
)


def farm_decision(
    crop,
    growth_stage,
    temperature,
    rain_probability,
    soil_moisture,
    disease_symptoms
):

    weather = weather_agent(
        temperature,
        rain_probability
    )

    soil = soil_agent(
        soil_moisture
    )

    crop_info = crop_agent(
        crop,
        growth_stage
    )

    disease = disease_agent(
        disease_symptoms
    )

    market = market_agent(crop)

    recommendations = []

    if soil_moisture < 30 and rain_probability < 60:
        recommendations.append(
            "Check the field and consider irrigation."
        )

    if temperature >= 35:
        recommendations.append(
            "Monitor the crop for heat stress."
        )

    if disease_symptoms.lower() == "yes":
        recommendations.append(
            "Inspect affected plants and seek agricultural expert advice."
        )

    if not recommendations:
        recommendations.append(
            "Continue monitoring soil, weather and crop conditions."
        )

    return {
        "Weather Agent": weather,
        "Soil Agent": soil,
        "Crop Agent": crop_info,
        "Disease Agent": disease,
        "Market Agent": market,
        "Recommendations": recommendations
    }
