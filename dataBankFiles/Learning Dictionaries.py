# Learning Dictionaries

##cca = []
##cca = ["BasketBall":"Sports1", "drama":"Perform1", "football":"Sports2"]
##
##del cca["BasketBall"]

# Exercises

# Exercise 1
##students = {}
##nameAndIndexNumber = input('Enter the name and index number of the student (comma-separated) or type 0 to stop adding: ')
##while nameAndIndexNumber != "0":
##    name = ''
##    commaHit = False
##    indexNumber = ''
##    for char in nameAndIndexNumber:
##        if char != ',':
##            if not commaHit:
##                name += char
##            else:
##                indexNumber += char
##        else:
##            commaHit = True
##    indexNumber = int(indexNumber)
##    students[indexNumber] = name
##    nameAndIndexNumber = input('Enter the name and index number of the student (comma-separated) or type 0 to stop adding: ')
##    
##
##print(' ')
##indexNumberToGetItem = input('Enter the index number to get the student name: ')
##print(' ')
##print('Student Name: {}\nStudent Index Number: {}'.format(students[indexNumber], indexNumber))

# Exercise 2: Building a Periodic Table
def element_ar():
    periodicTable = {}
    elementNameAndAtomicNumber = input('Enter the element\'s name and atomic number (comma-separated) or type 0 to stop building the Periodic Table: ')
    while elementNameAndAtomicNumber != "0":
        name = ''
        commaHit = False
        atomicNumber = ''
        for char in elementNameAndAtomicNumber:
            if char != ',':
                if not commaHit:
                    name += char
                else:
                    atomicNumber += char
            else:
                commaHit = True
        atomicNumber = int(atomicNumber)
        periodicTable[name] = atomicNumber
        elementNameAndAtomicNumber = input('Enter the element\'s name and atomic number (comma-separated) or type 0 to stop building the Periodic Table: ')
    print(' ')
    print('Periodic Table: ')
    # Printing the periodic table
    for element in periodicTable:
        numSpaces = 9 - len(element)
        if numSpaces <= 0:
            numSpaces = ' '
        else:
            numSpaces = ' ' * numSpaces
        print('{}{}{}'.format(element, numSpaces,periodicTable[element]))
    

# Exercise 3:Organic Mass Calculator

def organic_calculator():
    molecularMasses = {
        "C":12,
        "H":1,
        "O":16
        }
    compound = input('Enter the hydrocarbon: ')

    c_index = compound.find('C')
    h_index = compound.find('H')
    o_index = compound.find('O')

    c_atoms = compound[c_index+1:h_index]
    h_atoms = compound[h_index+1:o_index]
    if o_index > 0:
        o_atoms = compound[o_index+1::]
        mr = int(c_atoms)*molecularMasses['C'] + int(h_atoms)*molecularMasses['H'] + int(o_atoms)*molecularMasses['O']
    else:
        mr = int(c_atoms)*molecularMasses['C'] + int(h_atoms)*molecularMasses['H']
        
    print(mr)            
                
            
            















    
