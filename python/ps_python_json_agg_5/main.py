min_age = None
for aircraft in aircrafts:
        if aircraft["used_in"] == "Military":
                if min_age is None or aircraft["age"] < min_age:
                        min_age = aircraft["age"]
print(f"The age of youngest military aircraft is {min_age}")
