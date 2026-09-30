count = 0
for aircraft in aircrafts:
        if aircraft["used_in"] == "Military":
                count += 1
print(f"Count of military aircraft: {count}")
