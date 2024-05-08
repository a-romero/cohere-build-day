from langchain.tools import tool

@tool("Get garage address from name")
def get_garage_location(garage_name):
    """
    API for garage info data. Receives a garage name and returns its address
    """
    # Mock database in JSON format
    data = [
        {"garage": "AB Repairs", "address": "7 New St, Horsham RH13 5DT, UK"},
        {"garage": "ShowMeTheMoney Ltd", "address": "Faygate Ln, Faygate RH12 4SH"},
        {"garage": "WeFixEveryCar", "address": "Unit 5, Eagle Estate, Brooker's Rd, Billingshurst RH14 9RZ"}
    ]

    # Search for the cost of the specified part
    for record in data:
        if record["garage"] == garage_name:
            return f"{record['address']}"

    return "Garage not found"