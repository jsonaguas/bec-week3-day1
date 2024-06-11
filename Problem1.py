itinerary1 = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
def itinerary_check(itinerary):
    for x in range(len(itinerary)):

        traveler_name = itinerary[x][0]
        city1 = itinerary[x][1]
        city2 = itinerary[x][2]

        print(f"Itinerary {x+1}: {traveler_name} - From {city1} to {city2}")
itinerary_check(itinerary1)


