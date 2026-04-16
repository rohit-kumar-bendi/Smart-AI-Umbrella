import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATE_FILE = os.path.join(BASE_DIR, "shared", "state.json")


def read_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def write_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)
