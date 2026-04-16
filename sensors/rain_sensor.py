

import random


def is_raining():


    rain_detected = random.choice([True, False])

    return rain_detected


if __name__ == "__main__":
    rain_status = is_raining()
    print(f"Simulated Rain Detected: {rain_status}")
