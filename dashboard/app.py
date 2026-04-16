from flask import Flask, render_template, redirect, request, jsonify
import json
import os
import csv
import time

app = Flask(__name__)

STATE_FILE = "../shared/state.json"
CSV_FILE = "../data_log.csv"

start_time = time.time()


# ---------------------------
# READ STATE
# ---------------------------
def read_state():
    if not os.path.exists(STATE_FILE):
        return {}

    with open(STATE_FILE, "r") as f:
        return json.load(f)


# ---------------------------
# WRITE STATE
# ---------------------------
def write_state(data):
    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------
# CROP SAFETY SCORE
# ---------------------------
def crop_score(state):

    score = 100

    if state.get("temperature", 0) > state["config"]["temp_threshold"]:
        score -= 20

    if state.get("soil") == "DRY":
        score -= 20

    if state.get("rain") and state.get("soil") == "MOIST":
        score -= 10

    return max(score, 0)


# ---------------------------
# DASHBOARD
# ---------------------------
@app.route("/")
def index():

    state = read_state()

    alerts = []

    if state.get("temperature", 0) > state["config"]["temp_threshold"]:
        alerts.append("High Temperature Detected")

    if state.get("rain"):
        alerts.append("Rain Detected")

    if state.get("soil") == "DRY":
        alerts.append("Soil Dry – Irrigation Recommended")

    uptime = int(time.time() - start_time)

    log_count = 0

    if os.path.exists(CSV_FILE):
        with open(CSV_FILE) as f:
            log_count = sum(1 for _ in f) - 1

    score = crop_score(state)

    # SYSTEM STATUS
    system_status = {
        "temperature_sensor": "SIMULATED",
        "rain_sensor": "SIMULATED",
        "soil_sensor": "SIMULATED",
        "motor_controller": "READY",
        "decision_engine": "ACTIVE",
        "dashboard": "RUNNING"
    }

    return render_template(
        "index.html",
        mode=state.get("mode"),
        temperature=state.get("temperature"),
        rain=state.get("rain"),
        soil=state.get("soil"),
        umbrella=state.get("umbrella"),
        temp_threshold=state["config"]["temp_threshold"],
        soil_mode=state["config"]["soil_mode"],
        alerts=alerts,
        uptime=uptime,
        log_count=log_count,
        score=score,
        decision_message=state.get("decision_message"),  # ← decision explanation
        system_status=system_status
    )


# ---------------------------
# CONTROL ROUTES
# ---------------------------
@app.route("/auto")
def auto_mode():

    state = read_state()
    state["mode"] = "AUTO"

    write_state(state)

    return redirect("/")


@app.route("/manual")
def manual_mode():

    state = read_state()
    state["mode"] = "MANUAL"

    write_state(state)

    return redirect("/")


@app.route("/open")
def open_umbrella():

    state = read_state()

    if state["mode"] == "MANUAL":
        state["umbrella"] = "OPEN"

    write_state(state)

    return redirect("/")


@app.route("/close")
def close_umbrella():

    state = read_state()

    if state["mode"] == "MANUAL":
        state["umbrella"] = "CLOSED"

    write_state(state)

    return redirect("/")


# ---------------------------
# CONFIG UPDATE
# ---------------------------
@app.route("/update_config", methods=["POST"])
def update_config():

    state = read_state()

    state["config"]["temp_threshold"] = int(request.form["temp_threshold"])
    state["config"]["soil_mode"] = request.form["soil_mode"]

    write_state(state)

    return redirect("/")


# ---------------------------
# SENSOR GRAPH DATA
# ---------------------------
@app.route("/sensor-data/<sensor>")
def sensor_data(sensor):

    values = []

    if os.path.exists(CSV_FILE):

        with open(CSV_FILE) as f:

            reader = csv.DictReader(f)

            for row in reader:

                if sensor == "temperature":
                    values.append(float(row["temperature"]))

                elif sensor == "soil":
                    values.append(1 if row["soil"] == "MOIST" else 0)

                elif sensor == "rain":
                    values.append(1 if row["rain"] == "True" else 0)

    return jsonify(values[-20:])


# ---------------------------
# RUN SERVER
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)