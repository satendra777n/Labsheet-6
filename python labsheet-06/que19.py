import itertools
my_set = {1, 2, 3} # defining a set with elements 1 to 3
power_set = [] # initializing an empty list to store the power set
for i in range(len(my_set) + 1): # iterating through all possible lengths of combinations
    power_set.extend(itertools.combinations(my_set, i)) # adding combinations of length i to the power set
    
print("Power set:", power_set) # displaying the power set
