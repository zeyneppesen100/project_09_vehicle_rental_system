import json
import uuid
def load_vehicles(path:str) -> list:
    try:
        with open(path, "r", encoding="uts-8") as f:
            return json.load(f)
    except print("file error"):
        return none


def save_vehicles(path: str, vehicles: list) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(vehicles, f) #dump function converts a python object into a json formatted string

def add_vehicle(vehicles: list, vehicle_data: dict):
    vehicle = {
        "id": str(uuid.uuid4()),
        "make": vehicle_data["make"],
        "model": vehicle_data["model"],
        "year": vehicle_data["year"],
        "type": vehicle_data.get("type", "car"),
        "mileage": vehicle_data.get("mileage", 0),
        "status": "available",
        "rate_per_day": vehicle_data.get("rate_per_day", 0),
        "rate_per_km": vehicle_data.get("rate_per_km", 0),
        "features": vehicle_data.get("features", [])
    }

    vehicles.append(vehicle)
    return vehicle

def update_vehicle(vehicles: list, vehicle_id: str, updates: dict) -> dict:
    for v in vehicles:
        if v["id"] == vehicle_id:
            v.update(updates)
            return v
    if not v in vehicles:
       raise ValueError("Vehicle not found.")



def set_vehicle_status(vehicles: list, vehicle_id: str, status: str) -> dict: #??
    for v in vehicles:
        if v["id"] == vehicle_id:
            v["status"] = status
            return v
    raise ValueError("Vehicle not found.")

def list_available_vehicles(vehicles: list, rental_dates: tuple[str, str], vehicle_type: str | None = None) -> list:
    available_vehicles = []
    for v in vehicles:
        if v["status"] == "available" and (vehicle_type is None or v["type"] == vehicle_type):
           available_vehicles.append(v)
    return available_vehicles