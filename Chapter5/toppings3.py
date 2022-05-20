available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

final_toppings = []

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
        final_toppings.append(requested_topping.title())
    else:
        print(f"Sorry, we don't have {requested_topping}.")
        
print(f"\nFinished making your pizza!\
 Your pizza toppings are {final_toppings}.")