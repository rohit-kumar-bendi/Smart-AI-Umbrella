import json
import time
import random
import csv
import os

STATE_FILE = "shared/state.json"
CSV_FILE = "data_log.csv"


def read_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def write_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)


def get_temperature():
    return round(random.uniform(20, 40), 2)


def get_rain():
    return random.choice([True, False])


def get_soil():
    return random.choice(["DRY", "MOIST"])


def log_csv(temp, rain, soil, umbrella):

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["temperature","rain","soil","umbrella"])

        writer.writerow([temp, rain, soil, umbrella])


def main():

    print("=== Smart AI Umbrella System Started ===")

    while True:

        state = read_state()

        temperature = get_temperature()
        rain = get_rain()
        soil = get_soil()

        state["temperature"] = temperature
        state["rain"] = rain
        state["soil"] = soil

        decision = ""
        action = ""

        if state["mode"] == "AUTO":

            threshold = state["config"]["temp_threshold"]

            if rain:

                if soil == "DRY":

                    state["umbrella"] = "CLOSED"
                    action = "Umbrella closed"
                    decision = "Rain detected but soil dry → allowing natural irrigation"

                else:

                    state["umbrella"] = "OPEN"
                    action = "Umbrella opening"
                    decision = "Rain detected and soil moist → protecting crops"

            elif temperature > threshold:

                state["umbrella"] = "OPEN"
                action = "Umbrella opening"
                decision = "High temperature detected → crop protection activated"

            else:

                state["umbrella"] = "CLOSED"
                action = "Umbrella closed"
                decision = "Weather conditions normal → no protection required"

        else:

            decision = "Manual mode active"
            action = "User controlled"

        state["decision_message"] = decision
        state["umbrella_action"] = action

        write_state(state)

        log_csv(temperature, rain, soil, state["umbrella"])

        print("\n--- Sensor Update ---")
        print("Temperature:", temperature)
        print("Rain:", rain)
        print("Soil:", soil)
        print("Action:", action)
        print("Reason:", decision)

        time.sleep(5)


if __name__ == "__main__":
    main()