import json
import os
from datetime import datetime

def load_state(base_dir):
    os.makedirs(base_dir, exist_ok=True)
    def load_file(filename):
        path = f"{base_dir}/{filename}"
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    vehicles = load_file("vehicles.json")
    customers = load_file("customers.json")
    reservations = load_file("reservations.json")

    return vehicles, customers, reservations
def save_state(base_dir, vehicles, customers, reservations):
    with open(f"{base_dir}/vehicles.json", "w", encoding="utf-8") as f:
        json.dump(vehicles, f, indent=4)
    with open(f"{base_dir}/customers.json", "w", encoding="utf-8") as f:
        json.dump(customers, f, indent=4)
    with open(f"{base_dir}/reservations.json", "w", encoding="utf-8") as f:
        json.dump(reservations, f, indent=4)

def backup_state(base_dir, backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    files = ["vehicles.json", "customers.json", "reservations.json"]
    backups = []
    for file in files:
        src = f"{base_dir}/{file}"
        dst = f"{backup_dir}/{timestamp}_{file}"
        with open(src, "r", encoding="utf-8") as fsrc:
            data = json.load(fsrc)
        with open(dst, "w", encoding="utf-8") as fdst:
            json.dump(data, fdst, indent=4)
        backups.append(dst)
    return backups
