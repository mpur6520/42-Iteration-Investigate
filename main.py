#maru puran
#november 2 2023
#investigate a program in order to see how operators variables and functions and loops can work together to make a functioning and working program

number = 7 #declare and initilize the variable number, makes the value equal to 7
print("I'm thinking of a number, can you guess it?") #print statement, prints the words "i'm thinking of a number, can you guess it?" on the output console for the user to see and read
guess = int(input()) #declare and initilize the variable guess, stores the user's answer with the user's input and changes it into an integer using int() 
while guess != number: #begins the loop with the function while, checks if the variable guess is not equal to the variable number (or, if the user guesses wrong) and if this is true then it will trigger the code in the loop (!= means not equal to, so any number the user inputs if it's not equal to the number 7)
  print("Wrong! Guess again!") #print statement outputs message on the console log, prints the words "wrong! guess again!" on the output console for the user to see and read #inside the loop
  guess = input() #intializes the guess variable with a new input from the over (overrides it), but unlike line 7 it does not convert the user's answer to an integer because of the lack of int() #inside the loop
print("You guessed it!") #outside the loop #print statement outputs message on the console log, prints the words "you guessed it!" for the user to see and read

#if the usr enters something like "two" instead of of the actual number (a word), there will be a value error because it can't be converted from a string into an integer for line 7

#if the user enters 7 on their second or third (wherever they are in the loop)'s try it will still be marked as wrong, because it's taken as a string "7" not an integer 7. -- to fix this, you'd have to put an int() around the input() for the guess = input() inside of the loop on line 10

                                                #     /\______/\
# - - - - - - - - - - - - - - - - - - - - - - - - -  | o     o |
# - - - - - - - - - - - -                            |    w    |
                                            #        \_________/
# Give the line number where iteration starts.
  # Answer: The iteration starts in line 4 because the while statement is written there.

# What does '!=' mean?
  # Answer: The != operator means not equal to -- it's checking if guess the user inputs is not equal to the number (7), and runs the indented code if this is true.

# How many variables are there in the code?
  # Answer: There are 2 variables in the code, guess and number. They both hold integer values, guess is changed based on the user input and number is already established as 7.

# How can you tell which lines of code are inside the loop?
  # Answer: We can tell because the lines beneath the loop will be indented -- lines 9 and 10 are indented which means they're inside the loop.

# How many times will the loop repeat?
  # Answer: It terminates based on user input, it will keep going and looping until the user types in the number 7, then will print "You guessed it!" from line 7. It will loop repeat as many times as needed until the user types in the number 7. 

#But because line 10 doesn't convert the user's guess into an integer, it's just stored as a string. It won't be terminated because a string 7 isn't equal to a integer 7, the condition will never be false.

# What has to happen to make the program run the last line of code?
  # Answer: To make the program run the last line of code the while loop needs to terminate; this will only occur if the user enters the correct guess, 7, assigning it to the variable guess which is compared to number -- because the condition is false (7 equals 7,  so guess does equal number), the last line of code will be run.