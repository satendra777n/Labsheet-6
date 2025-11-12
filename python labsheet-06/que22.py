my_list = [1, 2, 2, 3, 4, 4, 5]
duplicates = set([x for x in my_list if my_list.count(x) > 1]) # finding duplicate elements by checking count in the list

print("Duplicate elements:", duplicates) # displaying the duplicate elements
