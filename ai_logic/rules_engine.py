def decide_umbrella_action(
    temperature,
    is_raining,
    light_intensity,
    soil_moisture,
    temp_threshold=35,
    soil_mode="DRY",
    light_mode="HIGH"
):
    

    
    if is_raining:
        return "OPEN"

    
    if temperature >= temp_threshold:
        return "OPEN"

    
    if soil_moisture == soil_mode:
        return "OPEN"

    
    if light_intensity == light_mode:
        return "OPEN"

    return "CLOSE"
