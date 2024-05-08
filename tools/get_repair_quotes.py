from langchain.tools import tool

@tool("Get repair quotes for vehicle parts")
def get_repair_quotes(make, model, year, part):
    """
    API for vehicle part repair quotes. Receives a make, model, year and part
    and returns a list of quotes for the part repair
    """
    # Mock database in JSON format
    data = [
        {"garage": "AB Repairs", "make": "Toyota", "model": "Camry", "year": "2020", "part": "bumper", "cost": 250},
        {"garage": "ShowMeTheMoney Ltd", "make": "Toyota", "model": "Camry", "year": "2020", "part": "bumper", "cost": 300},
        {"garage": "WeFixEveryCar", "make": "Toyota", "model": "Camry", "year": "2020", "part": "bumper", "cost": 240},

        {"garage": "AB Repairs", "make": "Toyota", "model": "Corolla", "year": "2019", "part": "door", "cost": 300},
        {"garage": "ShowMeTheMoney Ltd", "make": "Toyota", "model": "Corolla", "year": "2019", "part": "door", "cost": 320},

        {"garage": "WeFixEveryCar", "make": "Ford", "model": "Fiesta", "year": "2018", "part": "windshield", "cost": 200},
        {"garage": "ShowMeTheMoney Ltd", "make": "Ford", "model": "Fiesta", "year": "2018", "part": "windshield", "cost": 220},

        {"garage": "AB Repairs", "make": "Ford", "model": "Explorer", "year": "2021", "part": "hood", "cost": 550},
        {"garage": "WeFixEveryCar", "make": "Ford", "model": "Explorer", "year": "2021", "part": "hood", "cost": 500}
    ]

    quotes = []
    # Search for the cost of the specified part
    for record in data:
        quote = {}
        if record["make"] == make and record["model"] == model and record["year"] == year and record["part"] == part:
            quote['garage'] = record['garage']
            quote['cost'] = record['cost']
            quotes.append(quote)
            
    if not quotes:
        return "Part not found"
    else:
        return quotes