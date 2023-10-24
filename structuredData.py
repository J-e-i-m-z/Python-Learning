#LISTS
fruits = ["fig", "banana", "lemon"]
numbers = [1,2,3]

print(fruits[0])
print(numbers)

numbers[1] = 3
print(numbers)

fruits[2] = "mango"
print(fruits)
fruits[0:2] = "grapes","passion", "beetroot"
print(fruits)
fruits.insert(1, "orange") #INSERT FUNCTION - TO INSERT AN ITEM TO A LIST AT A SPECIFIED INDEX
print(fruits)

# Adding values to a list
fruitss = ["fig", "banana", "lemon"]
fruitss.append("watermelon")
print(fruitss)

newFruits = ["watermelon", "cherry"]
fruitss.extend(newFruits)
print(fruitss)

#Remove item from a list 
cars = ["mercedes", "bugatti", "ferarri"]
cars.remove("bugatti")
print(cars)
cars.insert(1, "bugatti")
print(cars)

newCars = ["Allion", "Toyota"]
cars.extend(newCars)
print(cars)
cars.append("Auris")
print(cars)

cars.pop(2) # REMOVES ITEM USING INDEXING
print(cars)
cars.pop() # REMOVES LAST ITEM IN THE LIST
print(cars)
#TUPLES - Almost similar to lists: ORDERED, UNCHANGEBLE(IMMUTABLE), ALLOW DUPLICATES

#SETS - STORE MULTIPLE VALUES: UNORDERED(CANNOT BE ACCESSED USING INDEXING), IMMUTABLE, DO NOT ALLOW DUPLICATES

#DICTIONARIES - UNORDERED (CNNOT BE ACCESSED USING INDEXING), CHANGEABELE, DO NOT ALLOW DUPLICATES