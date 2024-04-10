#Interview Questions
#List - collection of items(Duplicate is allowed

# list index start from 0

my_list = [1,2,3]

# it can multiple type of data types
my_list2 = ["Sherine", 4, True]

# indexing
print("Element at index 0 is ", my_list[0])

# changing an Element
my_list[1] = 20
print("After changing the element at index 1:", my_list)

# append()  => Add in the end
my_list.append(4)
print("List after appending", my_list)

# extend() => add a list  to the list
my_list.extend([5,6])
print("List after extending:", my_list)

# insert() => we can insert in the index
my_list.insert(1,'a')
print("List after inserting 'a' at index 1:",my_list)

# remove() => remove the
my_list.remove('a')
print("list after removing 'a'", my_list)


# Make a copy of the list
my_copy_list = my_list.copy()
print("copy list",my_copy_list)

# clear a list
#my_list.clear()
print("initial list",my_list)  # intial list cleared
print("copy list ",my_copy_list)

print("Index of value 3 in the list",my_copy_list.index(3))

# sort
my_copy_list.sort()
print("sorted list",my_list)

# reverse
my_copy_list.reverse()
print("reverse List",my_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
print(my_copy_list[4])
print(my_copy_list[5])

