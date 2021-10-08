###############################
# Types of construct ##########
###############################

# 1. Sequential construct --> stepwise
# 2. Iteration construct --> loop/repetition
# 3. Selection Construct --> decision

# Iteration Construct #
# 1. Indefinite loop #
#      - Iterations that last infinitely
#      - a terminating condition is usually required
#####################################################

# WHILE loop (indefinite)
# - condition must be able to terminate

##while <condition>:
##    <executable commands>
##    <remember to have a terminating condition>
#
#
# continue --> just move on to the next iteration
# break --> exit the entire while loop
##
##running = True
##stamina = 100
##injury = 0
##rest = 0
##while stamina > 0: # if stamina is >0, continue running
##    print("Running...")
##    if injury == "y":
##        print("Please stop running")
##        break
##    else:
##        if rest == "y":
##            print("Take a break for 5 mins")
##            rest = input("Do u need a rest? (y/n) ")
##            continue
##    stamina = int(input('Enter your stamina: '))
##    injury = input("Do you have any injury? (y/n) ")
##    rest = input("Do you need a rest? (y/n) ")
##    
##print("Running exercise has ended.")
# 2. Definite loop #
#    - runs a program for a fixed number of times
#    - shortcut in Python for arrays using in

# 1st way to use a For Loop #
# E.g print a series of numbers from 1 to 20 #

##for i in range(<length of range>):
##    <executable commands>

##for i in range(1, 21, 2):
##    print(i)

# 2nd way to use a For Loop #

##for i in range(20): #using range with length will start from 0 to length - 1
##    print(i)
    
# 3rd way: Shortcut in Python #
colour_lst = ['blue', 'orange', 'green', 'yellow']
for i in colour_lst:
    print(i)











