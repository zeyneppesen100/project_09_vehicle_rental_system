from datetime import datetime
import json

def to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def utilization_report(reservations, vehicles, period):
    start, end = period
    start = to_date(start)
    end = to_date(end)

    report = {}

    for v in vehicles:
        rented_days = 0

        for r in reservations:
            if r["vehicle_id"] != v["id"]:
                continue
            if r["status"] != "completed":
                continue

            restart = to_date(r["start_date"])
            reend = to_date(r["end_date"])

            overlap_start = max(start, restart)
            overlap_end = min(end, reend)

            if overlap_start <= overlap_end:
                rented_days += (overlap_end - overlap_start).days + 1

        total_days = (end - start).days + 1
        utilization = rented_days / total_days if total_days > 0 else 0

        report[v["id"]] = {
            "vehicle": f"{v['make']} {v['model']}",
            "utilization_rate": round(utilization, 2)
        }
    return report

def revenue_summary(reservations, period):
    start, end = period
    start = to_date(start)
    end = to_date(end)
    revenue = 0
    for r in reservations:
        if r["status"] != "completed":
            continue
        rs = to_date(r["start_date"])
        re = to_date(r["end_date"])
        if rs >= start and re <= end:
            revenue += r["invoice"]["total"]
    return {
        "total_revenue": revenue
    }

def upcoming_returns(reservations, reference_date):
    ref = to_date(reference_date)
    upcoming = []
    for r in reservations:
        if r["status"] == "active":
            end = to_date(r["end_date"])
            if end >= ref:
                upcoming.append(r)
    return upcoming

def export_report(report, filename): #export to json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    return filename












