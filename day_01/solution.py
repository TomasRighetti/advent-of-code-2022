# 1. Create an elfs dictionary to store each one with it's value
elfs = {}

# 2. Define the counter for the number of elfs
elf = 1

# 3. Open the elfs_calories file and read elf-by-elf storing their calories inside the dictionary
with open("elfs_calories.txt", "r") as elfs_calories:
	for index, calorie in enumerate(elfs_calories):
		if calorie == '\n':
			elfs[index] = 0
	

