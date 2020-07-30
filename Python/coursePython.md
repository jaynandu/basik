## Conditional steps
1. Ask question if
result true
2. then (elif)

> translation: if the first question is true. verify the second one.
3. Otherwise (else)
> translation: last option of condition if the previous statements are false

## Indentation

- Increase indent indent after an if statement or for statement(after :)
- Maintain indent to indicate the scope of the block(which lines are affected by the if/for)
- Reduce indent back to the level of the if statement of for statement to indicate the end of the block
- Blank lines are ignored - they do not affect indentation
- comments on a line by themselves are ignored with regard to indentation

# Python functions

- There are two kinds of functions in Python.
- Built-in functions that are provided as part of Python - print(), input(), type(), float(), int() ...
- Functions that we define ourselves and then use
- We treat the built-in function names as "new" reserved words (i.e, we avoid them as variables names)
  
## Function Definition

- In Python a function is some reusable code that takes arguments (s) as input, does some computation, and then returns a result or results
- We define a function using the def reserved word
- We call/invoke the function by using the function name, parentheses, and arguments in an expression.
  

## Building our own functions

- We create a new function using the def keyword followed by optional parameters in parentheses
- We indent the body of the function
- This defines the function but does not execute the body of the function
  
## Parameters

A parameter is a variable which we use in the function definition. It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.

## Return Values

Often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this. 
- A "fruitful" function is one that produces a result (or return value)
- The return statement ends the function execution and "send back" the result of the function

# Guidelines

To function or not to function

- Organize your code into "paragraghs" - capture a complete thought and "name it"
- Don't repeat yourself - make it work once and then reuse it
- If something gets too long or complex, break it up into logical chunks and put those chunks in functions
- Make a library of common stuff that you do over and over - perhaps share this with your friends...

## Loops and Iteration

- Loops (repeated steps) have iteration variables that change each time through a loop. Often these iteration variables go through a sequence of numbers. 

## Breaking Out of a Loop

- The break statement ends the current loop and jumps to the statement immediately following the loop
- It is like a loop test that can happen anywhere in the body of the loop
  
## Finishing an Iteration with continue

The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration. 

## Indefinite Loops

- **While** loops are called "indefinite loops" because they keep going until a logical condition becomes False
- The loop we have seen so far are pretty easy to examine to see if they will terminate or if they will be "infinite loops"
- Sometimes it is a little harder to be sure if a loop will terminate. 

## Definite Loops 

- Quite we have a list of items of the lines in a file - effectively a finite set of things 
- We can write a loop once for each of the items in a set using the Python **for** construct
- These loops are called "definite loops" because they execute an exact number of times
- We say that "definite loops iterate though the members of a set"
- Definite loops (for loops) have explicite **iteration variables** that change each time through a loop. These *iteration variables* move through the sequence or set. 

## Looking at In ...
- The *iteration variable* "iterates " through the *sequence*(ordered set)
- The block (body) of code is executed once for each value **in** the *sequence*
- The *iteration variable* moves through all of the values **in** the *sequence*

> 'code' 
> for i in [5, 4, 3, 2, 1] : 
		print(i)

		i stand for Iteration variable
		Five-element sequence

# Strings

## String Data Type

- A string is a sequence of characters
- A string literal uses quotes 'Hello' or "Hello"
- For strings, + means "concatenate"
- When a string contains numbers, it is still a string
- We can convert numbers in a string into a number using **int()**
`code`

str1= "Hello"
str2='there'
bob = str1 + str2
print(bob)
answers: Hellothere
*convert integer to number*
str3 = '123'
x = int(str3) + 1
print(x)
answers: 124

## Reading and converting

- we prefer to read data in using **strings** and then parse and convert the data as we need
- This gives us more control over error situations and/or bad user input 
- Raw input numbers must be **converted** from strings



> aka **str**

## Looking Inside Strings

- We can get any single character in a string using an index specified in **square brackets**
- The index value must be an integer and starts at zero
- The index value can be an expression that is computed
- The strings Have Length.
> The built-in **len** give us the length of a string
> 
> `code`
> 
> fruit ='banana
> 
> print(len(fruit))

- **Len Function** 
- A *Function* is *some stored code* that we use. A function takes some **input** and produces an **output**.
## Looping Through Strings
- Using a while statement and an iteration variable, and the len function, we can construct a loop to look at each of the letters in a string individually
- a definite loop using a **for** statement is much more elegant
- The iteration variable is completely taken care of by the **for** loop

## Looking deeper into *in*

- The *iteration variable* "iterates" through the sequence (ordered set)
- The *block (body) of code is executed once for each value *in* the **sequence**
- The *iteration variable* moves through all the values **in** the *sequence*

## Slicing Strings

- We can also look at any continuous section of a string using a colon operator
- The second number is one beyond the end of the slice- "up to but not including"
- If the second number is beyond the end of the string, it stops at the end. 

## Using *in* as a logical Operator

- The **in** keyword can also be used to check to see if one string is "in" another string
- The **in** expression is a logical expression that returns True or False and can be used in an if statement. 

- Python has a number of string functions which are in the string library
- These functions are already built into every string - we invoke them by appending the function to the variable
- These functions do not modify the original string, instead they return a new string that has been altered. 

# Reading Files

## Opening a File

* Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file
* This is done with the **open()** function
* open() returns a "file handle" - a variable used to perform operations on the file
* Similar to File -> Open" in a Word processor

### Using open()

* handle = open(filename, mode)
* returns a handle use to manipulate the file 
* filename is a string
* mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file

`code`

fhand = open('mbox.txt', 'r')

> you can open, read , write, close mbox.txt

##  The newline Character

* We use a special character called the "newline" to indicate when a line ends
* We represent it as \n in strings
* Newline is still one character - not two

## File Handle as a sequence

* A **file handle** open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
* We can use the for statement to iterate through a sequence 
* remember - a sequence is an ordered set 

'code'
xfile = open('mbox.txt')
 for cheese in xfile:
    print(cheese)


## Counting Lines in a File

* Open a file read-only
* Use a for loop to read each line
* Count the lines and print out the number of lines

`code`
fhand = open('mbox.txt')
count = 0
for line in fhand:
	count = count + 1
print('Line count:', count)

* The quit() is function for silent exit without trace back.
  
### Programming

* Algorithms: A set of rules or steps used to solve a problem
* Data structures: a particular way of organizing data in a computer
## List

A list is kind of Collection
* A collection allow us to put many values in a single "variable"
* A collection is nice because we can carry all many values around in one convenient package.
  `code` 
  friends= ['Joseph, 'Glenn', 'Sally']
  carryon = ['socks', 'shirt', 'perfume']

  * String are "immutable" - We  cannot change the contents of a string - we must make a new string to make any change
  * Lists are "mutable" - we can change an element of a list using the **index** operator

## List constants

* List constants are surrounded by square backets and the elements in the list are separated by commas
* A list element can be any python object - even another list
* A list can be empty


## How long is a List?

* The len() function takes a list as a paramater and returns the number of elements in the list
*  Actually len() tells us the number of elements of any set or sequence (such as a string...)
  
  Using the range function

* The range function returns a list of numbers that range from zero to one less than the parameter
* We can construct an index loop using for and an integer iterator
## Building a List from Scratch

* We create an empty **list** and then add elements using the **append** method
* The **list** stays in order and new elements are **added** at the end of the **list**
* There are a number of functions built into Python that take lists as parameters
* Best Friends : Strings and Lists

**splits** breaks a string into parts and produces a list of strings. We think of these as words. We can **access** a particular word or **loop** through all the words.

# Dictionaries

## What is a collection?

* A collection is nice because we can put more than one value in it and carry them all around in one convenient package
  
* We have a bunch of values in a single "variable"

* We do this by having more than one place "in" the variable

* We have ways of finding the different places in the variable

* Dictionaries are Python's most powerful data collection
* Dictionnaries allow us to do fast database-like operations in Python
* Dictionaries have different names in different languages
* Associate Arrays - Perl/ PHP 
* Propreties or Map or HashMap - Java
* Proprety Bag - C#/ .Net

* Lists **index** their entries based on the position in the list
* Dictionaries are like bags - no order
* So we index the things we put in the dictionary with a "lookup bag"



  











