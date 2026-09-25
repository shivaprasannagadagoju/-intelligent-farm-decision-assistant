def weather_agent(temperature, rain_probability):
    if rain_probability >= 60:
        return "Rain is likely. Avoid unnecessary irrigation."

    if temperature >= 35:
        return "High temperature detected. Monitor the crop for heat stress."

    return "Weather conditions are currently normal."


def soil_agent(soil_moisture):
    if soil_moisture < 30:
        return "Soil moisture is low. Irrigation may be required."

    if soil_moisture > 80:
        return "Soil moisture is high. Avoid excessive irrigation."

    return "Soil moisture is within the monitored range."


def crop_agent(crop, growth_stage):
    return (
        f"{crop} is currently in the {growth_stage} stage. "
        "Continue monitoring crop development."
    )


def disease_agent(disease_symptoms):
    if disease_symptoms.lower() == "yes":
        return (
            "Possible disease symptoms detected. "
            "Inspect affected plants and consult an agricultural expert."
        )

    return "No disease symptoms reported."


def market_agent(crop):
    return (
        f"Market analysis for {crop} can be connected "
        "to a live market-price API in a future version."
    )
