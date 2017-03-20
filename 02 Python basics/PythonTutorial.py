#Hi there! This is a basic tutorial in python
# The current text you are reading is not code, but comments.

# Comments are plain-text (i.e. not code) labels in a document and have to be 
## marked by putting # at the front of the line.

# The comments in this document will provide some labels, some narration, and 
## some guidance on the basic functions of python.

# Note: This tutorial assumes you are working in Enthought Canopy or some other
## python console environment where you can copy and paste code into python and 
## run them. This can often be accomplished by hitting Ctrl-Shift-R when the 
## relevant code is highlighted


# Python is an object based programming language. 

# This means that most objects or things you interact with, from basic numbers 
## through spreadsheets, have two types of information associated with them: 
## values and methods.

## Values are the what - an integer may have a value of 7; a string may have
### a value of 'potsherd
## Methods are the functions an object can carry out on its own. Just like in 
### math, functions generally take an input of some sort and return a new value
### or transform an object. A method for a string might be .upper(); 
### 'potsherd'.upper() returns 'POTSHERD'


# There are several types of values objects can take. The following are just a sampling:

# This is a string; it is a text object. Strings need to be surrounded by double or single quotes ("",'')
'five' 
"six"
# If we want to see what type of value this is, we can call the type() function on an object
print(type('five'))

#This should return <type 'str'>, where 'str' stands for string. To test this, we can run the following:
type('five')==str

#Here, str stands for the string object class; the type of any text object is str
# We use the == symbol to stand for an equality test; 1==1 returns True; 1==2 returns False

#The same holds true for numbers. Numbers can be one of two types: int, or integer, and float, or floating point (decimals)
5
5.5

print(type(5))
print(type(5.5))
print(type(5)==int)
print(type(5.5)==int)
print(type(5.5)==float)

#There are also more complicated data structuers that can store multiple values 
## at once. The big ones are tuples, lists, dictionaries, and arrays.

# Tuples are ways of storing a finite number of numbers. A tuple is a good 
## representation for geographic coordinates; while you don't know what the 
## coordinates might be, you know there will never be more than two. While it is
## easy to store and retrieve values, it is hard to change them. Tuples are 
## always made by putting objects inside of parentheses and separated by commas

print((5,6))
print(type((5,6)))

# Lists can store any number of items, and it is possible to add, remove, or 
## change values easily. Lists are made by separating values with commas and
## surrounding them with square brackets []

print([5,6])
print(type([5,6]))

# Lists and tuples are both indexed (accessible) by integers referring to the 
## position of the entry in the tuple or list. The first entry is numbered 0,
## the second 1, and so on (this is a computer science convention.)
## So, :
print([5,6][0])
print([5,6][1])

# TA DA!

# By contrast, dictionaries store entries according to keys. You can think of a 
## dictionary object as functioning like a real dictionary: there is a word 
## you look up, called a key, and en entry associated with that key, called a
## value.

{5: 'five', 6 : 'six'}

# In this example, 5 is the key and 'five' is the value of the first entry, 
## while 6 is the key and 'six' is the value of the second. Dictionary values
## are accessed by calling the key of the dictionary:

{5: 'five', 6 : 'six'}[6]


# So, in a flash, you have now learned the basic built in types of data
## structures in python. Congrats! You should feel free to use this and other 
## guides when you need to look these up. 



###FUNCTIONS AND VARIABLES ###

# We are now going to turn our attention to functions and variables.

# If we want to make any of these objects stay around for more than one line of
## code, we have to store them somewhere. We do this by defining variables.

# Creating a variable is easy: just create a phrase (settlement_size) and assign
## it a value using the = sign

settlement_size = 6
print(settlement_size)

# This also holds for more complex structures, like lists

sherd_count_list = [17,99,1,1,1,1,0,30]
print(sherd_count_list)
print(sherd_count_list[1])

# And if we really want to get crazy, we can nest structures inside of other structures

sherd_type_by_site = [[50,20,30],[11,29,60],[33,33,34]]
print(sherd_type_by_site)
print(sherd_type_by_site[0])

# Great! So we now have the ability to store data in our code and recall it 
## later, but what can we do with it? This is where functions come in.


### FUNCTIONS###

# As mentioned briefly earlier, functions carry out operations, generally on
## objects like those we've been exploring and creating. There are several
## built in functions related to numbers (sum, min, max), as well as many 
## methods built in to strngs (.upper, .lower). 

# There will only ever be a few functions that you need to know and memorize;
## functions are a great thing to google and to make your own resources for, as 
## you will ultimately figure out which functions are most useful for you.

print(sum(sherd_count_list))

# Python has thousands of functions, most of which are stored in modules that 
## you import in each script (that way they aren't overwhelming). NetworkX, 
## a module specifically designed for working with networks, is one that we 
## will be using later, as is pandas, a module designed for reading 
## spreadsheets.

# Modules are always imported using the import function, and are often 
## shortened to two-letter codes to make them easier to use

import string as st
print(st.capwords('i need my title formatted please'))

# Tl;dr learn modules and functions on an as-needed basis.


### OPERATORS ###

# There are also several operators you will want to be aware of that will make 
## your life easier. The most important concern iteration.

# Presumably you want to work with datasets that are tedious to work with by 
## hand, which is why network theory and python sound appealing to you. 

# In order to do that, you'll often find yourself needing to loop through 
## every row in a spreadsheet, or across every site in a survey. All of these
## involve using the for loop.

my_message = ['pretty','neat',"ain't",'it','?']
for text in my_message:
    print(text) 

# The for loop has a particular construction, or syntax, associated with it, 
## which requires six components

# 1. The clause always starts with the word for (hence the name)
# 2. The second word is always a variable that will take on the values of the
##      thing being iterated over (e.g. the name of every site)
# 3. The third word is always in (since the site name is IN this list of sites)
# 4. The fourth entry is always a list of objects OR an iterator (more on this.)
# 5. The clause always ends with a colon (to mark the beginning of the loop)
# 6. The next line is indented and starts the code of what happens each loop

# So in our example above, the variable text takes on the values of the list
## my_message. For every value, it runs a single function, print, which prints
## that entry. 

# We can also run a for loop with a more complex code
 
my_message = ['pretty','neat',"ain't",'it','?']
for text in my_message:
    text_exciting = text.upper()
    text_exciting += '!!!' #This is an easy way of adding to a string
    print(text_exciting)
