import json

dirtyname = ['📈eurusd📉', 'buy', '@', '(1.11271)', 'sl:', '1.11020', '(24)', 'tp:', '1.11754', '(50)']

cleanname = json.dumps(dirtyname)
print(cleanname)


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3, 0, 5, 6]

# Print all items from list_1 that are not in list_2 ()
print(*[item for item in list_1 if item not in list_2], sep='\n')

# Print all items from list_1 that differ from the item at the same index in list_2
print(*[x for x, y in zip(list_1, list_2) if x != y], sep='\n')

# Print all items from list_2 that differ from the item at the same index in list_1
print(*[y for x, y in zip(list_1, list_2) if x != y], sep='\n')

