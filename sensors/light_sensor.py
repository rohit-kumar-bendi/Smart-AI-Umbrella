import random

def get_light_intensity():
    light_levels = ["LOW", "MEDIUM", "HIGH"]
    light_intensity = random.choice(light_levels)


    return light_intensity

if __name__ == "__main__":
    light = get_light_intensity()
    print(f"Simulated Light Intensity: {light}")
    