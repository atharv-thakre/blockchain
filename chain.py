import json
import hashlib
import os
from datetime import datetime

FILE_NAME = "records.json"


def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def load_chain():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []


def save_chain(chain):
    with open(FILE_NAME, "w") as f:
        json.dump(chain, f, indent=4)


def get_previous_hash(chain):
    if len(chain) == 0:
        return "GENESIS_BLOCK"

    return chain[-1]["current_hash"]


def add_record(action, officer, details):
    chain = load_chain()

    timestamp = str(datetime.utcnow())

    previous_hash = get_previous_hash(chain)

    block_data = f"{timestamp}{action}{officer}{details}{previous_hash}"

    current_hash = calculate_hash(block_data)

    block = {
        "timestamp": timestamp,
        "action": action,
        "officer": officer,
        "details": details,
        "previous_hash": previous_hash,
        "current_hash": current_hash
    }

    chain.append(block)
    save_chain(chain)

    print("Block Added Successfully")
    print(json.dumps(block, indent=4))


if __name__ == "__main__":
    add_record(
        action="Complaint Resolved",
        officer="Officer_101",
        details="Pothole issue fixed in Ward 12"
    )