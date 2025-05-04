import json

def load_keywords():
    with open("config/keywords.json", "r") as file:
        keywords = json.load(file)
        return keywords