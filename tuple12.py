tupl = "w", 3, "r", "s", "o", "u", "r", "c", "e"
tuplex = tupl[:2] + tupl[3:]
list = list(tupl) 
list.remove("c") 
tupl = tuple(list)
print(tupl)