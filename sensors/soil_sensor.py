import random


def get_soil_moisture():
    moisture_levels = ["DRY", "MOIST", "WET"]
    soil_moisture = random.choice(moisture_levels)

    return soil_moisture

if __name__ == "__main__":
    moisture = get_soil_moisture()
    print(f"Simulated Soil Moisture Level: {moisture}")