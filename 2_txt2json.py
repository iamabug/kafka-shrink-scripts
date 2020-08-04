import json

obj = {}
obj["version"] = 1
obj["topics"] = []
with open("topics.txt") as f:
    for line in f.readlines():
        topic = {"topic": line.strip()}
        obj["topics"].append(topic)

with open("topics.json", "w") as f:
    json.dump(obj, f, indent=2)
