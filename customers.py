import json
import uuid

def load_customers(path: str) -> list:
    try:
        with open(path,"r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_customers(path: str,customers: list) -> None:
    with open(path, "w",encoding="utf-8") as f:
        json.dump(customers, f)

def register_customer(customer: list, profile: dict) -> dict:
    customer = {
        "id": str(uuid.uuid4()),
        "name": profile["name"],
        "license_number": profile["license_number"],
        "pin": profile["pin"],
        "phone": profile.get("phone"),
        "email": profile.get("email"),
        "rentals": []
    }
    customers.append(customer)
    return customer
def authenticate_customer(customers: list, license_number: str, pin: str) -> dict | None:
    for x in customers:
        if x["license_number"] == license_number and x["pin"] == pin:
            return x
    return None

def update_customer_profile(customers: list, customer_id: str, updates: dict) -> dict:
    for x in customers:
        if x["id"] == customer_id:
            x.update(updates)
            return x
    raise ValueError("customer not found")



