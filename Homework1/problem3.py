# Exercise 1: Create the list ​a ​with the following values: ​1, 4, 5, 7, 8, -2, 0, -1

a = [1, 4, 5, 7, 8, -2, 0, -1]

# Exercise 2: Print the values of list ​a ​at indices ​3 ​and 5​

print("Value at 3rd index:", a[3], '\n', "Value at 5th index:", a[5])

# Exercise 3: Sort the list ​a ​in a decreasing order and assign 
#			  the newly obtained list to the variable ​a_sorted, ​
# 			  the list ​a ​should not be changed

a_sorted = a.copy()
a_sorted.sort(reverse = True)

# Exercise 4: Print the 2 sublists of the list ​a_sorted ​containing 
# 			  the indices 1...3 and 2...6

print("1 to 3 indices of a_sorted:", a_sorted[1:4], '\n',
	  "2 to 6 indices of a_sorted:", a_sorted[2:7])

# Exercise 5: Delete the values at indices ​2 ​and 3​ ​from ​a_sorted

del a_sorted[2:4]

# Exercise 6: Print the list ​a_sorted

print("Deleted values at indices 2 and 3", a_sorted)

# Exercise 7: Create the list ​b ​with the following values: ​
#			  “grapes”, “Potatoes”, “tomatoes”, “Orange”, 
#			  “Lemon”, “Broccoli”, “Carrot”, “Sausages”

b = ["grapes", "Potatoes", "tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]

# Exercise 8: Sort the list ​b ​in an increasing order and assign 
#			  the newly obtained list to the variable ​b_sorted, ​
#			  the list ​b ​should not be changed

b_sorted = b.copy()
b_sorted.sort()

# Exercise 9: Create a new list ​c​. The first 3 values of the list ​c​ 
#			  should be the elements from the list ​a ​at indices 1...3 
#			  and the last values of the list ​c ​should be the elements 
#			  from the list ​b ​at indices 4...6.

c = a[1:4] + b[4:7]

# Exercise 10: Print the list ​c

print("The list c is", c)
