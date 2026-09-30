for person in people:
        total_age += person["age"]
        count += 1
average_age = total_age / count if count > 0 else 0
print(f"Average age: {average_age:.2f}")
