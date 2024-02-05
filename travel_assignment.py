import itertools

def find_cheapest_flight(destination="Bali", flexibility_days=3, budget=2000, preferred_airlines=None):
    flight_options = []

    airlines = ["Garuda Indonesia", "Singapore Airlines", "AirAsia", "Lion Air"]
    dates_range = range(-flexibility_days, flexibility_days + 1)

    date_combinations = list(itertools.product(dates_range, repeat=2))

    for departure_date, return_date in date_combinations:
        price = 1500  
        baggage_allowance = 20  
        layover_duration = 3  
        flight_rating = 4.5

        flight_details = {
            "airline": airlines[date_combinations.index((departure_date, return_date)) % len(airlines)],
            "departure_date": "2024-07-01",  
            "return_date": "2024-07-15"  
        }

        if price <= budget:
            if preferred_airlines is None or flight_details["airline"] in preferred_airlines:
                flight_options.append({
                    "price": price,
                    "details": flight_details,
                    "baggage_allowance": baggage_allowance,
                    "layover_duration": layover_duration,
                    "flight_rating": flight_rating
                })

    sorted_flight_options = sorted(flight_options, key=lambda x: x["price"])

    top_3_options = sorted_flight_options[:3]
    for i, option in enumerate(top_3_options, start=1):
        print(f"Option {i}:")
        print(f"Airline: {option['details']['airline']}")
        print(f"Price: ${option['price']}")
        print(f"Departure Date: {option['details']['departure_date']}")
        print(f"Return Date: {option['details']['return_date']}")
        print(f"Baggage Allowance: {option['baggage_allowance']} kg")
        print(f"Layover Duration: {option['layover_duration']} hours")
        print(f"Flight Rating: {option['flight_rating']}")
        print("\n")

find_cheapest_flight(preferred_airlines=["Garuda Indonesia", "Singapore Airlines"])