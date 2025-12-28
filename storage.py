import json
import os
from datetime import datetime

def load_state(base_dir):
    with open(f"{base_dir}/vehicles.json", "r", encoding="utf-8") as f:
        vehicles = json.load(f)
    with open(f"{base_dir}/customers.json", "r", encoding="utf-8") as f:
        customers = json.load(f)
    with open(f"{base_dir}/reservations.json", "r", encoding="utf-8") as f:
        reservations = json.load(f)
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