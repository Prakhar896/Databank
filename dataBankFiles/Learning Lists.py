# Learning Lists
# we have talked about: int, float, char, boolean, str, lists

# LISTS
# a type of array that can be used to house many other #
# different types of data #
# List of integers: [23, 354, 23, 930]
# List of strings: ["blue", "orange", "red"]
# List of lists: [[1,2,4,5], ["sahaa"]]
# Lists are mutable --> can be changed

##lst = ['a', 'b', 'c']
##lst[0] = "A" # --> lists atre mutable, elements can be changed
##print(lst)


# Types of operations for a list #
##################################
# 1. Indexing  #
#       - same as string. Index start from 0 #
# 2. Slicing #
#       - same as strings.

##lst = [1, 2, 3, 4, 5, 6]
##print(lst[:3])
##
### 3. Concatenation #
###       - same as strings.
##lst1 = ["a", "b"]
##lst2 = ["c", "D"]
##print(lst1 + lst2)
###           * Note for Concatenation *
###               - you need to convert to a list type before concatenating #
##lst3 = [5, 6, 7, 8]
##lst3 = lst3 + [9]
##print(lst3)
##
### 4. Repetition #
###       - same as strings.
##
##lst4 = ["a", 1]
##print(lst4*2)

#######################################
# Common List Method That Can Be Used #
#######################################
# 1. To find the length of a lisr #
#       - len[<lst_name>]
##lst = [1, "s", 4, 6, [1, 2, 3]]
##print(len(lst)) # prints "5"
##print(len(lst[4])) # prints length of sub-list which is at index 4, prints "3"



# 2. To add elements to a list --> Concatenation

##lst = ["a", "b", "c"]
###       to add in "d" to the list
###       (A) Use concatenation
####lst = lst + ["d"] # or lst = lst + list("d")
##
###       (B) The append method
##lst.append("d") # --> actionable method, does not return a value

# 3. To extract the last element from a list

##lst = [3, 6, 10, 83, -1]
###       (A) Slicing
####lst = lst[0:4]
####print(lst) # prints [3, 6, 10, 83]
###       (B) Pop
##lst.pop()
##print(lst) # prints [3, 6, 10, 83]


# 4. Sorting
##num_lst = [397, 45, 1, 34, 67]
##num_lst.sort()
##print(num_lst)
##num_lst.sort(reverse = True)
##print(num_lst)

# 5. Find Max Value
##lst = [2, 5, 56, 23, 53]
### Method 1: Sort and then use Indexing
##lst.sort()
##print(lst[-1]) # prints 56
### Method 2: Loops
##maxValue = 0
##for value in lst: # Shortcut in Python --> Only works if you do not need indexing
##    if value > maxValue:
##        maxValue = value
##print(maxValue) # prints 56
### Range version of For Loop Method:
##largest = 0
##for i in range(len(lst)):
##    if lst[i] > largest:
##        largest = lst[i]
##print(largest)
### Method 3: max() method
##print(max(lst)) # Using max function to find maximum value
### Extra: use min() to find minimum value
##print(min(lst)) # Using min function to find minimum value

### 6. Count number of elements appear
##survey_lst = ["red", "blue", "green", "blue", "yellow"]
##print(survey_lst.count("blue")) # prints 2 --> blue appears twice

### 7. Insert eleements within a list
##cca_lst = ["badminton", "basketball", "drama", "chinese orchestra"]
### E.g. Insert volleyball in between basketball and drama
##cca_lst.insert(2, "volleyball")
### cca_lst.insert(<index_no_to_insert>, <element>]
##print(cca_lst) # prints updated list







































