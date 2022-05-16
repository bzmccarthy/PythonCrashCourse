cars = ['bmw', 'audi', 'toyota', 'subaru']

# cars.sort(reverse = True)

print(f"Here is the original list, {cars}.")

print(f"\nHere is the sorted list: {sorted(cars, reverse = True)}.")

print(f"\nHere is the original list again, {cars}.")

cars.reverse()

print(f"Original list in reverse order, {cars}.")