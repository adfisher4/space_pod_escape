import random

print("\n\n\n\n   Space Pod Escape \n\n\n")

print("You're locked in a space pod and oxygen levels are running low.  Use your master decoding skills to break out of the space pod to your oxygen-rich SpacePlex! \n\n")

print("You have 12 tries to decode the lock on the space pod before oxygen runs out.  The code is 3 digits between 100 and 999, with some helpful clues after each guess to help you narrow it down. \n")

#Newly generated code to guess for each game.
pod_code = str(random.randint(100, 1000))
turns = 12

def game_on(pod, turns): 
    #Force Correct Input
    try:
        attempt = int(raw_input("Choose a 3 digit numerical code: "))  
        #Validating a three-digit integer was entered.
        if attempt > 99 and attempt < 1000:
            attempt_string = str(attempt)
            turns -= 1
            correct_location = 0
            #Attempt matches the pod code. Game won!
            if attempt_string == pod:
                print("\n\nCongratulations!!! You have unlocked the space pod using %s! Enjoy the extra space and all that oxygen! \n\n " % (pod))
                exit()
            #Player ran out of turns
            elif turns == 0: 
                print("\n\nSorry, you're last guess was incorrect and you are out of turns.  The pod code was: %s \n\n" % (pod))
                exit()
            #For-each loop to detect how many digits match in the correct place value.
            for x in range(len(attempt_string)):
                if attempt_string[x] == pod[x]:
                    correct_location += 1

            else:
                print("\nYou have found {} digit/s in the correct place value. You have {} turns remaining \n".format(correct_location, turns))
        
        else:
            print("\n\nYour attempt should be at least 100 and at most 999.  Try again!\n")

    #Force Correct Input
    except (TypeError, ValueError, NameError):
        print("\n\n That is an invalid attempt.  Try again\n")

    game_on(pod, turns)
        
game_on(pod_code, turns)