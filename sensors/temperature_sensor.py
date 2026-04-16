import random


def get_temperature():

    temperature = random.uniform(25.0, 40.0)

    return round(temperature, 2)

if __name__== "__main__":
    temp = get_temperature()
    print(f"simulated Temperature: {temp} °C")