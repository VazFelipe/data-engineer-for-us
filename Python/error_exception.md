# Contents

- [Contents](#contents)
- [Guided-project by Coursera](#guided-project-by-coursera)
- [Requirements](#requirements)
- [The difference between Errors and Exceptions in Python Code](#the-difference-between-errors-and-exceptions-in-python-code)
    - [Error](#error)
    - [Exception](#exception)
- [Raising and exception when a condition occurs](#raising-and-exception-when-a-condition-occurs)
  - [Assert error exception](#assert-error-exception)
  - [Try and except block](#try-and-except-block)
  - [Try and except block with else clause](#try-and-except-block-with-else-clause)
  - [Try and except block with else and finally clauses](#try-and-except-block-with-else-and-finally-clauses)
- [Important to know (I received 83,33%)](#important-to-know-i-received-8333)

# Guided-project by Coursera

- Course: [Exception Handling in Python](https://www.coursera.org/projects/exception-handling-in-python)
- Tutor: [Emma Martin](https://www.linkedin.com/in/emmamartinbelfast/)

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# Requirements

- Basic python programming skills

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# The difference between Errors and Exceptions in Python Code

- A Python code should terminates when it encounters an error. The developer should provide usefull information about the program behavior when the program is running.

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### Error

- A **syntax error** (a.k.a compile time errors) happens when the python interpreter try to run your program and during the execution it encounters an error. The interpreter will print the information about the error in the terminal.

> For example, in your python IDE run:
 ```python 
 # it will raise an error like
 # SyntaxError: unmatched ')'
 
 print(15/5))

 # to solve the syntax error you have just to remove the extra ')' like this:

 print(15/5)
 ```

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### Exception

- An **exception** is just like something that can be parsed by the python interpreter, the code is correct, but for any reason it cannot run (a.k.a runtime error).

> For example, in your python IDE run:
 ```python 
 # it will raise an exception error like
 # ZeroDivisionError: division by zero
 
 print(15/0)
 ```

- Python has many built in exceptions that is accessible to create our exceptions and make our program more robust.

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# Raising and exception when a condition occurs

- In the following example, the program behavior is defined for only a person that is over 18 years old. To do this, whe should raise and exception when the condition less than 18 years old happens.

> For example, in your python IDE run:
```python
# you will be prompted to enter your name
name = input('Enter your name ')
# then your age
age = int(input('Enter your age '))
print('Your name is: '+name)
# then the program will set a condition
if age < 18:
    # and raise an error
    raise ValueError('Error: you need to be over 18')
else:
    # otherwise it will continue executing until the end
    print('Your age is: '+str(age))
```

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

## Assert error exception

- Based on our previous knowledge, we are going to learn how to build our debug message to provide usefull information about the program behavior when the program is running and to detect
problems early in your program development.

- The assert keywords allow the developer to test if a condition is true, and if not raise an assertion error.

> For example, in your python IDE run:
```python
def print_age(age):
    # the assert will allow that when the condition is not meet it will raise your exception
    assert age > 0, "The age has to be greater than zero."
    # otherwise it will continue executing until the end
    print("Your agen is: "+str(age))
```

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

## Try and except block

- When you are developing programs you will likely have syntax errors or exceptions as we have seen in the examples above. In this situations the try and except block is handy.

> For example, in your python IDE run:
```python
try:
    num1 = 4
    num2 = 0
    result = num1/num2
    print(result)
except ZeroDivisionError as e:
    print(e)
```

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

## Try and except block with else clause

- The else clause only executes if no exceptions were raised in the try and except block. 

> For example, in your python IDE run:
```python
try:
    # if a string was defined in the num1
    # then the exception occurs
    # otherwise, the else clause
    num1 = '4'
    num2 = 1
    result = num1/num2
    print(result)
    print('end of try block.')
except TypeError:
    print('ops, there is a TypeError.')
else:
    print('no exceptions were raised.')
```

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

## Try and except block with else and finally clauses

- The finally clause will always execute after the try and except block and else clause. We usually implement a finally clause to clean up the environment reserved to run the program, sych as close a connection, of close a file, etc... 

> For example, in your python IDE:
- create a file named example.txt in Documents folder
- get the path to this folder
- then adapt to the code below and run the program
- you will see that the program executes well
- but if you delete the example.txt and run the program again you will that the exception will be raised and the finally wil be executed.
```python
try:
    f = open('example.txt', encoding='utf-8')
except FileNotFoundError:
    print('FileNotFoundError')
finally:
    f.close()
```

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# Important to know (I received 83,33%)

- What is the meaning of an exception within code?
- What is the meaning of a syntax error within code?
- Using error and exception handling is used in production code for which reasons?
- What is meant by compile time errors? (syntax error)
- What is meant by raising an exception?
- Raising an exception is useful because ...
- What does an AssertionError exception mean? (false and then raise)
- Why is an AssertionError exception beneficial to developers?
- Why is using a try-except block effective?
- Does an else clause execute when there is an exception within the try block?
- Does a finally clause always execute?
- Why is a finally clause effective?

![certificate](/python/images/certificate.png)

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)