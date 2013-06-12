# Rock-paper-scissors-lizard-Spock
# Mini project #1


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        err_msg = "Invalid Entry <" + str(number) + ">"
        return err_msg


    
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        err_msg = "ERR: Invalid Entry <" + str(name) + ">"
        print err_msg
        return 99

import random

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    if (player_number == 99):
        print "ERR: Invalid Choice Entered!"
        print
        return 79

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)

    # compute difference of player_number and comp_number modulo five
    does_player_win = (comp_number - player_number) % 5

    # use if/elif/else to determine winner
    if (does_player_win == 3 or does_player_win == 4):
        player_wins = True
    elif (does_player_win == 1 or does_player_win == 2):
        player_wins = False
    elif (does_player_win == 0):
        player_wins = "Tie"
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
        
    # print results
    print 
    print "Player chooses " + name
    print "Computer chooses " + comp_name
    if ( player_wins == True):
        print "Player wins!"
    elif (player_wins == False):
        print "Computer wins!"
    elif (player_wins == "Tie"):
        print "Player and computer tie!"
        
    
   

    
# test number_to_name
#print number_to_name("spock")
#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)
#print number_to_name(5)

# test name_to_number
#print name_to_number("spock")
#print name_to_number("rock")
#print name_to_number("Spock")
#print name_to_number("paper")
#print name_to_number("lizard")
#print name_to_number("scissors")
#print name_to_number(7)

#ut rpsls

#rpsls("Rock")
#rpsls(3)
#rpsls("paper")
#rpsls("paper")
#rpsls("paper")

# test rpsls

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



# always remember to check your completed program against the grading rubric
#done

