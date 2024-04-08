# PPHA 30537
# Spring 2024
# Homework 1

# YOUR CANVAS NAME HERE: Taiyu Liu
# YOUR GITHUB USER NAME HERE: tliu520

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
My_list = ['Taiyu','Tianhao','Ziqiang']
for index, value in enumerate(My_list):
    print(f"The value at position {index} is {value}")

# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.
test_strings = [
    "redar",
    "A man, a plan, a canal, Panama!",
    "Microsoft",
    "This isn't a palindrome"
]
for s in test_strings:
    s_clean = ''.join(char for char in s if char.isalnum()).lower()
    s_reverse = s_clean[::-1]
    is_palindrome = s_clean == s_reverse
    print(f"The string '{s}' is a palindrome: {is_palindrome}")

# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')

available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
while True:
    choice = input('Please pick a vegetable I have available: ')
    if choice in available_vegetables:
        print(f'You can have the {choice}.')
        break
    else:print('That is not a valid choice. Please try again.')


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.
original_list= ['basketball', 'China','berry', 'apple', 'pencil']
filtered_list = [s.lower() for s in original_list if not s.lower().startswith(('a', 'b'))]
print(filtered_list)


    
# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL','IN','MI','WI']
long_names = ['Illinois','Indiana','Michigan','Wisconsin']
state_dictionary = {short_names[i]: long_names[i] for i in range(len(short_names))}
print(state_dictionary)


#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def evaluate_sum(num1, num2):
    the_sum = num1 + num2
    if the_sum > 10:
        return "big"
    elif the_sum == 10:
        return "just right"
    else:
        return "small"
start_list = [(10,0),(100,6),(0,0),(-15,-100),(5,4)]
result_list = [evaluate_sum(num1,num2) for num1, num2 in start_list]
print(result_list)

# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

def my_func(a):
    b = 40
    return a + b
x = my_func(10)
print(x)
#By passing the variable a as an argument, my_func 
#becomes more generic and does not depend on 
#external variables. This reduces the risk of errors due 
#to changing global variables and makes the behavior of functions more predictable and understandable.


# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random
import random
import string
def generate_password(length, special_chars=True, include_numbers=True):
    if not 8 <= length <= 16:
        return ("Invalid password length. Please choose a length between 8 and 16.")
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if special_chars: 
        characters += '!@#$%^&*'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print(generate_password(12))
  
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.
import random
class MovieDatabase:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.movie_list = []
    def add_movie(self, title, genre, rating):
        if 0 <= rating <= 5:
            self.movie_list.append((title,genre,rating))
        else:
            print("Rating should be between 0 and 5.")
    def what_to_watch(self):
        if not self.movie_list:
            print("No movie to recommend. Please add some movies first")
        else:
            movie = random.choice(self.movie_list)
            print(f"Tonight, {self.owner_name} recommends: {movie[0]} - a {movie[1]} rated {movie[2]}/5 starts.")
Taiyu_movies = MovieDatabase('Taiyu')
Taiyu_movies.add_movie('Forrest Gump', 'Comedy-Drama', 5)
Taiyu_movies.add_movie('Inception', 'Science Fiction', 4.5)
Taiyu_movies.add_movie('Gravity', 'Thriller', 4)
Taiyu_movies.add_movie('La La Land', 'Musical', 4.5)
Taiyu_movies.what_to_watch()
            