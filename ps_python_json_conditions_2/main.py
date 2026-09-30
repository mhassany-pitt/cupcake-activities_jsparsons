is_empty = True
for aircraft in aircrafts:
        if aircraft["used_in"].lower() == "military":
                print(f"Name: {youngest_military_aircraft["name"]}")
                is_empty = False
if is_empty:
        print("No military aircraft found.")
