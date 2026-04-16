
from config import settings

umbrella_state = "CLOSED"


def open_umbrella():
    global umbrella_state

    if umbrella_state == "OPEN":
        print("Umbrella is already OPEN.")
    else:
        print("Umbrella is OPENING...")
        umbrella_state = "OPEN"
        settings.UMBRELLA_STATUS = "OPEN"
        print("Umbrella is now OPEN.")


def close_umbrella():
    global umbrella_state

    if umbrella_state == "CLOSED":
        print("Umbrella is already CLOSED.")
    else:
        print("Umbrella is CLOSING...")
        umbrella_state = "CLOSED"
        settings.UMBRELLA_STATUS = "CLOSED"
        print("Umbrella is now CLOSED.")
