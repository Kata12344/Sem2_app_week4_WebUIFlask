from flask import abort, make_response

BOOKINGS = {
    "Barcelona2026":{
        "booking_id": "MyBarcelona2026",
        "holiday_id": "Barcelona2026",
        "transportation": "car",
        "num_people": "2",
        "customer_name": "Mari Mari" 
    }
}

def read_all():
    return list(BOOKINGS.values())

def create(booking):
    booking_id = booking.get("booking_id")
    holiday_id = booking.get("holiday_id")
    transportation = booking.get("transportation", "")
    num_people = booking.get("num_people", "")
    customer_name = booking.get("customer_name", "")

    if booking_id and holiday_id and transportation and num_people and customer_name not in BOOKINGS:
        BOOKINGS[booking_id] = {
            "booking_id": booking_id,
            "holiday_id": holiday_id,
            "transportation": transportation,
            "num_people": num_people,
            "customer_name": customer_name
        }
        return BOOKINGS[booking_id], 201
    else: 
        abort(
            406,
            f"Booking with booking_id {booking_id}, already exists"
        )


def read_one(booking_id):
    if booking_id in BOOKINGS:
        return BOOKINGS[booking_id],200
    else:
        abort(
            404, f"Booking with booking id {booking_id} not found, Available BOOKINGS keys: {list(BOOKINGS.keys())}"
        )

def update(booking_id, booking):
    if booking_id in BOOKINGS:
        BOOKINGS[booking_id]["customer_name"] = booking.get("customer_name",BOOKINGS[booking_id]["customer_name"])
        BOOKINGS[booking_id]["num_people"] = booking.get("num_people",BOOKINGS[booking_id]["num_people"])
        return BOOKINGS[booking_id]
    else:
        abort(
            404,
            f"Booking with booking id {booking_id} not found"
        )

def delete(booking_id):
    if booking_id in BOOKINGS:
        del BOOKINGS[booking_id]
        return make_response(
            f"{booking_id} sucessfully deleted", 200
        )
    else:
        abort(
            404,
            f"Booking with booking id {booking_id} not found"
        )