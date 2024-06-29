# Python Tutorials

## Conditional statements 
> The conditional statement available in python is if-elif-else

### Example
```py
if a > b :
    print("a is greater than b")
else:
    print("b is greater than a")
```

## Looping 
>There are two loops available in python
>- For loop
>- While loop

### Examples
for loop
```py
for i in range(3):
    print(i)
```
while loop
```py
while True:
    print("The statement is true")
```

>We can also include else statements for both the loops as else part will execute when the loop gets over

## Python Data Structures

### List
>Python Lists are just like the arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.

### Syntax
```py
lst = [1,2,"abc",12.4]
print(lst)
```
### List methods
```py
lst = [2,1,3]
#append method - Adds an element at the end of the list
lst.append(4)
#clear method - Removes all the elements from the list
lst.clear()
#count method - Returns the number of elements with the specified value
lst.count(1)
#pop method - Removes the element at the specified position
lst.pop()
#sort method - Sorts the list
lst.sort()
print(lst)
```
#### Output
```py
[2,1,3,4]
[]
1
[1,2,3,4]
```

### Tuple methods

> Most of the tuple methods will be same as list methods . The only difference between list and tuple is list is mutable but tuple is immutable

### Dictionary methods
```py
dictionary_1 = {"car" : "Honda" , "Model" : "2009"}
#values method - Returns a list of all the values in the dictionary
dictionary_1.values()
#keys method - Returns a list containing the dictionary's keys
dictionary_1.keys()
```
> clear() , copy() methods will be same as for lists

## Enumerate method

>The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

#### Example
```py
for index,item in enumerate(lst):
    print(f"{index}-{item}") #format string
```

#### Output
```py
1-item 1
2-item 2
3-item 3
```

## Working with text files

### Opening a file in python
```py
file = open("file.txt","r")
```

### File opening methods 
> - r
> - w
> - r+
> - w+
> - a

> Default file opening method is read mode (r)

### Reading contents from the file
- read() method
- readline() method
- readlines() method

### Example
```py
file = open("file.txt","r")
file.read() #Returns the read bytes in form of a string
file.readline() #Reads a line of the file and returns in form of a string.
file.readlines() #Reads all the lines and return them as each line a string element in a list.
```

### file.txt
```txt
hello
all 
welcome
```

### Output
```py
'helloallwelcome'
'hello'
['hello\n','all\n','welcome\n']
```

### Writing contents from the file
- write() method 
- writelines() method

### Example
```py
file = open("file.txt","w")
file.write("Hello") #Inserts the string str1 in a single line in the text file.
file.writelines(["Welcome\n","to\n","my page\n"]) #For a list of string elements, each string is inserted in the text file.Used to insert multiple strings at a single time.
```

### file.txt
```txt
HelloWelcome
to 
my page
```
## try and except block
>The try block lets you test a block of code for errors.<br>
>The except block lets you handle the error.

### Example
```py
try:
  print(x)
except NameError:
  print("Variable x is not defined")

```

> The above code will work good till it experiences a name error . When name error is spotted the except block will run and provide the output


## Custom Functions in python
>A function is a set of statements that take inputs, do some specific computation, and produce output. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can call the function.
> - In Python, a def keyword is used to declare user-defined functions. 
> - An indented block of statements follows the function name and arguments which contains the body of the function. 

### Example 
```py
# Declaring a function
def fun():
	print("Inside function")

# Calling function
fun()
```

## Some of the Python's important modules

### csv module
>CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database.

### Example
```py
import csv

with open("scores.csv", "r") as file:
    data = list(csv.reader(file))

user_value = input("Enter the batsman name to know the runs : ")
for batsman in data:
    if batsman[0] == user_value:
        print(f"{batsman[0]} scored {batsman[1]} runs ")
```
scores.csv
```csv
"Batsman","Runs"
"Virat Kohli","56"
"Rohit Sharma","92"
"Rishab Pant","57"
```

### Output
```
Enter the batsman name to know the runs : Virat Kohli
Virat Kohli scored 56 runs 
```

### glob module
>With the help of the Python glob module, we can search for all the path names which are looking for files matching a specific pattern (which is defined by us).

### Example
```py
import glob

myfiles = glob.glob("../textfile_b_example/*txt")
for i in myfiles:
    with open(i, "r") as f:
        print(f.read())
```

### Output
```py
Nice day :)

Mahendra Singh Dhoni
Rohit Sharma
temperature
2
4
5
4
5
Virat Kohli
```

### shutil module
>Shutil module offers high-level operation on a file like a copy, create, and remote operation on the file. It comes under Python’s standard utility modules.

### Example
```py
import shutil

shutil.make_archive("using_shutil", "zip", "../textfile_b_example")
```

### Output
>Created a zip file containing of all the files present in the specified directory


### webbrowser module
>The webbrowser module includes functions to open URLs in interactive browser applications.

### Example
```py
import webbrowser

user_input = input("Enter anything to search : ")
webbrowser.open(f"https://search.brave.com/search?q={user_input}&source=desktop")
```

### Output
> A web broswer will be opened and the search query will also be completed .


## Desktop GUI

> To create a desktop app using graphical user interface , we need a third party module known as FreeSimpleGUI. <br>
> We need to install the module explicitly in our machine .

```py
import FreeSimpleGUI as fsg
```


## Web Application
> To create a web application we need to install the third-party module known as streamlit . Streamlit is a third-party module which is used to make basic web applications

```py
import streamlit as st
```