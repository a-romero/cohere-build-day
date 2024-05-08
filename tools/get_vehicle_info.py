from langchain.tools import tool

@tool("Get vehicle info fom registration numbers")
def get_vehicle_info(registration_number):
    """
    API for vehicle info data. Receives a registration number a returns vehicle information
    """
    # Mock database in JSON format
    data = [
        {"registrationNumber": "AB123CDE", "make": "Toyota", "model": "Camry", "year": "2020", "address": "12 Gossops Parade, Crawley RH11 8HH, UK"},
        {"registrationNumber": "FG4234IJ", "make": "Toyota", "model": "Corolla", "year": "2019", "address": "Unit 17, Piries Place, Horsham RH12 1EH, UK"},
        {"registrationNumber": "KL345MNO", "make": "Ford", "model": "Fiesta", "year": "2018", "address": "Chapel Rd, Barns Green, Horsham RH13 0PS, UK"},
        {"registrationNumber": "PQ456RST", "make": "Ford", "model": "Explorer", "year": "2021", "address": "Newpound Ln, Wisborough Green, Billingshurst RH14 0EG, UK"}
    ]

    # Search for the cost of the specified part
    for record in data:
        if record["registrationNumber"] == registration_number:
            return f"{record['make']},{record['model']},{record['year']},{record['address']}"

    return "Vehicle not found"