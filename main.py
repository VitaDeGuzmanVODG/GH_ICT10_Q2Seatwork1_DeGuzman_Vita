# Student Club Member Checker
from unicodedata import name

from pyscript import display, document


def check_member(e):
    document.getElementById("result").innerHTML = ""
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = f"{first_name} {last_name}".strip()

    club_members = [
        "Destiny Math Demon",
        "Francheesecake Dela Cruz",
        "Raver Espanol Pistachio",
        "Santiago Kuya",
        "MJ Bronzer",
        "Kenneth Cabinet",
        "Bombalean Kahoot",
        "Jia Tickles",
        "Chalanie Absent",
        "Enrique Ray Cis",
        "Jack Jesse All"
    ]

    member_checker = full_name.casefold() in [
        name.casefold() for name in club_members
    ]

    messages = {
        False: f"Sorry {full_name}, your name is not in the Monarch Club member list.",
        True: f"Congratulations {full_name}, you are a member of the Monarch Club!"
    }

    display(messages[member_checker], target="result")