from datetime import datetime

def save_event(person_id):
    now = datetime.now()

    with open("logs/events.txt", "a") as file:
        file.write(
            f"{now.strftime('%Y-%m-%d %H:%M:%S')} | Person {person_id} entered restricted zone\n"
        )