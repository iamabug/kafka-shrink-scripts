import json
import random

BROKER_ID = 1005
BROKER_IDS = [1001, 1002, 1003, 1004]
n = len(BROKER_IDS)
topics = {}
with open("current.json") as f:
    topics = json.load(f)
    for partition in topics["partitions"]:
        replicas = partition['replicas']
        for i in range(len(replicas)):
            if replicas[i] == BROKER_ID:
                choice = random.randint(0, n-1)
                while BROKER_IDS[choice] in replicas:
                    choice = random.randint(0, n-1)

                print("before: ", replicas)
                replicas[i] = BROKER_IDS[choice]
                print("after: ", replicas)
                print()

with open("reassigned.json", "w") as f:
    json.dump(topics, f, indent=2)
