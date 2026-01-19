import json

data = {
    "name": "Suborna",
    "age": 23,
    "skills": ["Python", "ML", "CP"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)