import uuid
from datetime import datetime
def to_date(date_str):
    y, m, d = date_str.split("-")
    return date(int(y), int(m), int(d))
def check_availability(reservations, vehicle_id, star_date, end_date):
    start = to_date(start_date)
    end = to_date(end_date)
    for r in reservations:
        if r["vehicle_id"] != vehicle_id:
            continue
        existing_start = to_date(r["start_date"])
        existing_end = to_date(r["end_date"])
        if not (end < existing_start or start>existing_end):
            return False
    return True
def create_reservation(reservations, reservation_data, vehicles):
    vehicle_id = reservation_data["vehicle_id"]
    customer_id = reservation_data["customer_id"]
    start_date = reservation_data["start_date"]
    end_date = reservation_data["end_date"]
    if to_date(start_date)> to_date(end_date):
        raise ValueError
    if not vehicle_id in vehicles:
        raise ValueError #for non-existing vehicle
    reservation = {
        "id": str(uuid.uuid4()),
        "vehicle_id": vehicle_id,
        "customer_id": customer_id,
        "start_date": start_date,
        "end_date": end_date,
        "status": "active",
    }
    reservations.append(reservation)
    return reservation


def cancel_reservation(reservations, reservation_id):
    for r in reservations:
        if r["id"] == reservation_id:
            if r["status"] != "active":
                return False
            r["status"] = "canceled"
            return True
    return False

def days_between(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    return (end - start).days + 1
def complete_rental(reservations, reservation_id, return_data, vehicles):
    for r in reservations:
        if r["id"] == reservation_id and r["status"] == "active":
            for v in vehicles:
                if v["id"] == r["vehicle_id"]:
                    vehicle = v
                    break
            if vehicle is None:
                raise ValueError
            r["status"] = "completed"
            r["return_odometer"] = return_data.get("return_odometer")
            r["damages"] = return_data.get("damages", False)
            r["fuel_level"] = return_data.get("fuel_level", "full")
            vehicle["status"] = "available"
            vehicle["mileage"] = r["return_odometer"]

            return r
        raise ValueError

def calculate_invoice(reservation, vehicle):
    days = days_between(reservation["start_date"], reservation["end_date"])
    cost = days * vehicle["rate_per_day"]
    mileage_cost = 0
    if "return_odometer" in reservation and vehicle["rate_per_km"] > 0:
        mileage_cost = vehicle["rate_per_km"] * vehicle["mileage"]
    total = base_cost + mileage_cost
    return {
        "days": days,
        "cost": cost,
        "mileage_cost": mileage_cost,
        "total": total
    }