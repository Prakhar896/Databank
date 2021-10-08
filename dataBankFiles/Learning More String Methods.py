################
#String Methods#
################

# Methods: similar to functions, written in Python Library
#          methods require fixed input values and return fixed output values


## String Checking Methods ##
# check if the string contains alpha letters and numbers only
##ndp = "Singapore 56"
##print(ndp.isalnum()) # returns false as space is not considered as an alphabetical letter or number
##
##sch2 = "Ngee Ann"
##print(sch2.isalpha()) # returns false
##
### <str>/isdigit() #
### Check if the string contains numbers only #
### Note: This method is for strings only NOT for int #
##number = "12345"
##print(number.isdigit()) # returns True
##
### <str>.isspace() #
### Checks if the string contains space(s) only #
### Returns boolean value
##
##str1 = "      "
##print(str1.isspace()) # returns True
##str2 = "A     "
##print(str2.isspace()) # returns False

##a = "ABC"
##print(a.isupper()) # returns True
##
##b = "A B C"
##print(b.isupper()) # returns True
##
# <str>.islower() #
# checks if the string contains lowercase onlyt #
# returns a boolean
##
##a = "abc"
##print(a.islower()) # returns true
##
##b = "a b c"
##print(b.islower()) # returns True

# *** Spaces do not affect .isupper() or .islower() return values *** #
##############################################
# String Conversion Method ###################
##############################################

# <str>/upper() #
# Convert and return the original string in upper casing #
##a = "a B c"
##print(a.upper()) # returns "A B C"
##
### <str>.lower() #
### Connvert and return the original string in lower casing #
##b = "P Q R"
##print(b.lower()) # returns "p q r"
##
##c = "ab C 12"
##print(c.lower()) # returns "ab c 12" (numbers do not affect)
##
##d = "Hello!!"
##print(d.lower()) # return "hello!!"

########################
# String Check Methods #
########################

# <str.startswith()>
# Check if a string starts with a particular string segment #
# Return a boolean value

##code = 'COM1234'
##print(code.startswith('COM')) # returns True
##
### <str.endswith(<string_segment>)
##print(code.endswith('34')) # returns True

################################
# String Methods for Searching #
################################

# <str>.find(<string_segment>)
##name = "Alberto"
##print(name.find("b")) # returns 2
##
##name2 = "Robertbertberto"
##print(name.find("bert")) # returns 2 (always gives first segmemnt finding)
##
##name3 = "baba"
##print(name.find('z')) # returns -1 (not found in string)
# Search for the starting index of a segment #

###############################################
# String Methods to Process Strings (Data) ####
###############################################


# <str>.split(<segment>)
# Splits a string into smaller segments according to the segment defined

##greeting = "Hello, World!"
##print(greeting.split())
### returns a list ["Hello,", "World!"]
### by default splits by spaces
##
##countries = "Singapore, Malaysia, Indonesia"
##print(countries.split(', ')) # returns ["Singapore", "Malaysia", "Indonesia"]








