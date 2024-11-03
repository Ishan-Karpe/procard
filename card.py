# js one of my old projects from repl.it
# the reason i am doing this is because replit limited only 3 repls for free users so I am migrating most of my repls to github

import time

print("Welcome to ProCard - A Profile Card in the Python Console!")
time.sleep(0.5)

print("Question 1 out of 5:")
time.sleep(0.2)
your_name = input("What is your name? ")
print("Question 2 out of 5:")
time.sleep(0.2)
your_age = input("What is your age? ")
print("Question 3 out of 5:")
time.sleep(0.2)
city = input("What city do you live in? ")
print("Question 4 out of 5:")
time.sleep(0.2)
hobby = input("What is one hobby you like to do? ")
print("Question 5 out of 5:")
time.sleep(0.2)
food = input("What is your one favorite food out of all favorite foods? ")

time.sleep(1)
print("Generating Proflie Card")
time.sleep(0.3)
print("Generating Proflie Card.")
time.sleep(0.3)
print("Generating Proflie Card..")
time.sleep(0.3)
print("Generating Proflie Card...")
time.sleep(1)
print("Ok, Your Proflie Card is ready!")
time.sleep(0.5)

print(f"Name: {your_name}\nAge: {your_age}\nCity you live in: {city}\nHobby you like: {hobby}\nFavorite Food: {food}")
time.sleep(2.5)

rate = input("How would you like to rate this Proflie Card maker so far? 1, 2, 3, 4, or 5: ")
if rate == "1":
        print("Thanks for the", rate, "star, I will improve this repl,", your_name,"!!!")
elif rate == "2":
        print("Thanks for the", rate, "stars, I will improve this repl,",
              your_name,"!!!")
elif rate == "3":
        print("Thanks for the", rate, "stars, I will improve this repl,",
              your_name,"!!!")
elif rate == "4":
        print("Thanks for the", rate, "stars, I will improve this repl,",
              your_name,"!!!")
else:
        print("Thanks for the", rate, "stars", your_name,"!!!")