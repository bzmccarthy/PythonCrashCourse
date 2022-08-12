from die import Die

import matplotlib.pyplot as plt

# Create a d6
die = Die(num_sides=8)
die2 = Die(num_sides=8)

# Make some rolls, and store results in a list
results = []

for roll_num in range(100000):
    result = die.roll() + die2.roll()
    results.append(result)
    
# Analyze results
frequencies = []

for value in range(1+1, die.num_sides+die2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results
x_values = list(range(1+1, die.num_sides+die2.num_sides+2))
y_values = frequencies

    
print(frequencies)

plt.hist(x=results, bins = x_values)