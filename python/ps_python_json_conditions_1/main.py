shortest_duration = None
for flight in flights:
        if flight["from"] == "New York" and flight["to"] == "Pittsburgh":
                if shortest_duration is None or flight["duration"] < shortest_duration:
                        shortest_duration = flight["duration"]
if shortest_duration is not None:
        print(f"The shortest flight from New York to Pittsburgh is {shortest_duration} minutes.")
else:
        print("No flights found between New York and Pittsburgh.")
