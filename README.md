# One Line Art


**Hello There 👋**

<img src="/images/OneLineArt.jpg" alt="OneLineArt" title="sample" width="250" height="250" align="right" />

Have you heard anything about **The Art of One Line Drawing** Or **Single Line Drawing** Or maybe **Continuous Line Drawing**?

From [The art of one line drawings](https://medium.com/@michellegemmeke/the-art-of-one-line-drawings-8cd8fd5a5af7) :
> A one line drawing, also known as a single line drawing, is a drawing made with just one single, unbroken line.
> The most famous example even dates back to the early 20th century, the one line drawings made by Pablo Picasso. He took a complex, realistic example and simplified it into one single unbroken line. These drawings can look relatively simple to make, but capturing the true essence of the shape in just one line can be quite challenging.

Ain't It Fantastic? 😍 <br>
Just as we can draw any simple and complex drawing with one line, we can also implement different algorithms with just one line of code. Obviously, this is not a coding style, but it is clear that creating an algorithm in one line can be very challenging. Therefore, I'm saying that this is literally an art and not everyone can do it!  

<img src="/images/HelloWorld.jpg" alt="HelloWorld" title="HelloWorld" width="250" align="right" />

**Python** is one of the best choices to do this. You will soon understand why :)<br>
I will give you some basic ideas on how to do this, then we will share different questions with each other and try to solve it with a single line of code.
<br>It's gonna be very fun and challenging, believe me 😃
<br><br>

## Table of Contents  
- [Lambda Functions](#lambda-functions)
- [Input](#input)
- [Calling Functions](#calling-functions)
- [List Comprehension](#list-comprehension)
  - For Loops
  - While Loops
- [Recursive Functions](#recursive-functions)
- [Factorial](#factorial)

## Lambda Functions
First of all, You should learn about [lambda functions](https://www.w3schools.com/python/python_lambda.asp). Lambda functions play an important role in what we want to do

> Python lambdas are little, anonymous functions, subject to a more restrictive but more concise syntax than regular Python functions.
[Read more...](https://realpython.com/python-lambda/#lambda-calculus)

```py
>>> (lambda x, y: x * y)(2, 3)
6
>>> (lambda *args: sum(args))(*range(10, 20))
145
```

## Input
The first challenge you may face is getting input from the user and using it multiple times. Suppose we want to get a number from the user and bring it to the power of the same number. Normally we can do this as follows :

```py
n = int(input())
print(n ** n)
```
‍‍‍
But now you have to use lambda functions, see :
```py
print((lambda n: n ** n)(int(input())))
```

OR by using [`map()`](https://www.w3schools.com/python/ref_func_map.asp) :
```py
print(*map(lambda n: n ** n, [int(input())]))
```

## Calling Functions
You can use lists to call several different functions

Look at this simple code :
```py
a = int(input()) ** 2
a += int(input())
print(a)
```

Now Let's do it with a list :
```py
[a := int(input()) ** 2, a := a + int(input()), print(a)]
```

## List Comprehension
You can use list comprehension to create a for loop or while

A simple for loop :
```py
for i in range(1, 5):
  print(i * i)
```
List Comprehension :
```py
[print(i * i) for i in range(1, 5)]
```

A simple while loop :
``` py
a = 0
while a < 10:
  a += 1
  print(a)
```
List Comprehension :
```py
[(a := globals().get('a', 0) + 1, print(a)) for i in iter(lambda: globals().get('a', 0) < 10, False)]
```
You may want to read more about [`iter()`](https://www.w3schools.com/python/ref_func_iter.asp) and [`globals()`](https://www.w3schools.com/python/ref_func_globals.asp)

## Recursive Functions

This is a factorial recursive function :
```py
def factorial(x):
  return x if x <= 1 else x * factorial(x - 1)

>>> factorial(5)
120
```

Now Let's do this by lambda functions:
```py
>>> (lambda f: lambda x: f(f, x))(lambda f, x: x if x <= 1 else x * f(f, x - 1))
>>> _(5)
120
```

## Factorial

1. Using Recursive Functions
```py
def factorial(x):
    return x if x <= 1 else x * factorial(x - 1)

print(factorial(int(input())))
```
```py
print((lambda f: lambda x: f(f, x))(lambda f, x: x if x <= 1 else x * f(f, x - 1))(int(input())))
```
2. Using For loop
```py
a = 1
for i in range(1, int(input()) + 1):
    a *= i

print(a)
```
```py
print([a := i * globals().get('a', 1) for i in range(1, int(input()) + 1)][-1])
```
3. Using [`functools.reduce()`](https://docs.python.org/3/library/functools.html#functools.reduce)
```py
print(__import__('functools').reduce(lambda x, y: x * y, range(1, int(input()) + 1)))
```
You may want to read more about [`__import__()`](https://docs.python.org/3/library/functions.html#import__)


<br>
<div align="center">
  <img width="64" alt="LCoders | AmirHosseinAghajari" src="https://user-images.githubusercontent.com/30867537/90538314-a0a79200-e193-11ea-8d90-0a3576e28a18.png">
  <br><a>Amir Hossein Aghajari</a> • <a href="mailto:amirhossein.aghajari.82@gmail.com">Email</a> • <a href="https://github.com/Aghajari">GitHub</a>
</div>
