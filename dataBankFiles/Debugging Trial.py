message = input("enter a message: ")
punctuation_count = 0
for character in message:
    if not character.isalnum() and character != ' ':
        punctuation_count += 1

print(punctuation_count)


########################
# Test Cases ###########
########################

# user input --> Check for data validation
# Data Validation Checks: Lengeth, Presence, Format, Range #
#   1. Presence Check = ""
#   2. Length Check --> Overlaps with presence check
#   3. Format Check - types of characters
#       (aplhabetical, digits, punctuation, spaces)
#   4. range check --> Invalid as it only applies to numerical inputs
