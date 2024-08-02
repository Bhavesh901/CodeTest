3. #Write a Python function to count the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)

# Example usage
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2
count = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {count} times in the list.")

#Output
#The element 2 occurs 4 times in the list.
