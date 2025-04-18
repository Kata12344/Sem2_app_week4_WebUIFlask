from flask import abort

HOLIDAYS = {
    "Barcelona2026":{
        "ID": "Barcelona2026",
        "location": "Barcelona",
        "pricePP": "500",
        "availableDate": "2026-03-23" 
    },
    "Cyprus2034":{
        "ID": "Cyprus2034",
        "location": "Cyprus",
        "pricePP": "1400",
        "availableDate": "2034-11-10" 
    },
    "Paris2022":{
        "ID": "Paris2022",
        "location": "Paris",
        "pricePP": "850",
        "availableDate": "2022-01-02" 
    }
}

def read_all():
    return list(HOLIDAYS.values())

def create(holiday):
    ID = holiday.get("ID")
    location = holiday.get("location")
    pricePP = holiday.get("pricePP", "")
    availableDate = holiday.get("availableDate", "")

    if ID and location and pricePP and availableDate not in HOLIDAYS:
        HOLIDAYS[ID] = {
            "ID": ID,
            "location": location,
            "pricePP": pricePP,
            "availableDate": availableDate
        }
        return HOLIDAYS[ID], 201
    else:
        abort(
            406,
            f"Holiday with ID {ID}, already exists",
        )