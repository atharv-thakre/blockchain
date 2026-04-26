import json
import hashlib
import os

FILE_NAME = "records.json"


def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def load_chain():
    if not os.path.exists(FILE_NAME):
        print("records.json not found")
        return []

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        print("Invalid JSON file")
        return []


def verify_chain():
    chain = load_chain()

    if len(chain) == 0:
        print("No blockchain records found")
        return

    print("\nChecking Blockchain Integrity...\n")

    for i in range(len(chain)):
        block = chain[i]

        timestamp = block["timestamp"]
        action = block["action"]
        officer = block["officer"]
        details = block["details"]
        previous_hash = block["previous_hash"]
        stored_hash = block["current_hash"]

        # Recreate hash
        recalculated_data = f"{timestamp}{action}{officer}{details}{previous_hash}"
        recalculated_hash = calculate_hash(recalculated_data)

        # Check 1: Current hash integrity
        if stored_hash != recalculated_hash:
            print(f"❌ Hash mismatch detected at Block {i + 1}")
            print("Possible tampering found")
            return

        # Check 2: Previous hash chain link
        if i > 0:
            actual_previous_hash = chain[i - 1]["current_hash"]

            if previous_hash != actual_previous_hash:
                print(f"❌ Broken chain detected at Block {i + 1}")
                print("Previous hash does not match")
                return

    print("✅ Blockchain Verified Successfully")
    print("No tampering detected")


if __name__ == "__main__":
    verify_chain()