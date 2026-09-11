# Python Full Concept

A beginner-friendly Python script covering fundamental programming concepts with multiple code examples for each topic.

## Topics Covered

| Topic | Description |
|-------|-------------|
| **User Input** | Getting input from the user and displaying output |
| **Casting** | Converting between `str`, `int`, and `float` types |
| **Arithmetic Operators** | Basic math operations: `+`, `-`, `*`, `/` |
| **if / else** | Conditional statements with real-world examples |
| **elif** | Multi-branch conditions (grading, calculator) |
| **for Loop** | Iteration with `range()`, counting, summing, lists |
| **Nested Loops** | Loops inside loops (weekly schedule, patterns) |
| **while Loop** | Repeating code while a condition is true |

## File

| File | Description |
|------|-------------|
| `python_concepts.py` | All concept examples in a single script |

## How to Run

Make sure Python is installed, then run:

```bash
python python_concepts.py
```

> The script is interactive — it will prompt you for inputs as it runs through each concept.

## Python Basics for Beginners

A step-by-step introduction to the fundamentals of Python.

### 1. Single and Double Quotes

In Python, text is called a **string**. You can write a string using either **single quotes** (`'...'`) or **double quotes** (`"..."`).

```python
print('Hello')   # single quotes
print("Hello")   # double quotes
```

Both produce exactly the same result — Python treats them identically.

**When to use which?**
- If your text contains single quotes, wrap it in double quotes: `"It's raining"`
- If your text contains double quotes, wrap it in single quotes: `'He said "hi"'`

```python
print("It's a beautiful day")
print('She said "hello"')
```

### 2. Python Variables

A **variable** is a container used to store data — like a labelled box. You create one by giving it a name and assigning a value with the `=` sign.

```python
name = "Archana"     # string (text)
age = 20             # integer (whole number)
height = 5.5         # float (decimal number)
is_student = True    # boolean (True / False)
```

Once assigned, you can use the variable anywhere in your code:

```python
print(name)
print(age)
```

### 3. Getting the Type of a Variable

The `type()` function tells you what **data type** a variable is.

```python
print(type("Hello"))   # <class 'str'>
print(type(10))        # <class 'int'>
print(type(10.5))      # <class 'float'>
print(type(True))      # <class 'bool'>
```

Checking the type of existing variables:

```python
name = "Archana"       # str
age = 20               # int
height = 5.5           # float
is_student = True      # bool

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

| Example | Type | Meaning |
|---------|------|---------|
| `"Archana"` | `str` | Text (string) |
| `20` | `int` | Whole number |
| `5.5` | `float` | Decimal number |
| `True` | `bool` | True or False |

### 4. Rules for Python Variable Names

Follow these rules when naming a variable:

- Must start with a letter or an underscore (`_`).
- Cannot start with a number.
- Can contain letters, numbers, and underscores.
- Cannot contain spaces.
- Variable names are **case-sensitive** (`name`, `Name`, and `NAME` are different).
- Python keywords cannot be used as variable names (like `if`, `for`, `while`).

**Valid names:**

```python
name = "Archana"
_name = "Archana"
name1 = "Archana"
my_name = "Archana"
```

**Invalid names:**

```python
1name = "Archana"     # cannot start with a number
my name = "Archana"   # cannot contain a space
my-name = "Archana"   # cannot contain a hyphen
if = 10               # 'if' is a Python keyword
```

### 5. Multi-Word Variable Names

To create a variable name with more than one word, join the words with an underscore (`_`):

```python
first_name = "Archana"
student_age = 20
college_name = "Anna University"
```

Multi-word names made with underscores are clear and easy to read.

### 6. Python Naming Conventions

There are three common ways to write multi-word names:

**Camel Case** — first word lowercase, next words start with a capital letter:

```python
firstName = "Archana"
studentAge = 20
```

**Pascal Case** — every word starts with a capital letter:

```python
FirstName = "Archana"
StudentAge = 20
```

**Snake Case** — all lowercase, words separated by underscores:

```python
first_name = "Archana"
student_age = 20
```

> **Tip:** In Python, `snake_case` is the most commonly used style for variable names.

### 7. Python Output

The `print()` function displays information in the console.

```python
print("Hello World")
print("My name is Archana")
print(10)
print(10 + 20)
```

You can also print variables:

```python
name = "Archana"
age = 20

print("Name:", name)
print("Age:", age)
```

You can print multiple things in one line by separating them with commas:

```python
print("Name:", name, "Age:", age)
```

### 8. Python Input

The `input()` function lets the user type information into the program. The text inside the parentheses is the question (prompt) shown to the user.

```python
name = input("Enter your name: ")
print("Hello", name)
```

**Important:** `input()` always returns a **string** — even if the user types a number.

```python
name = input("Enter your name: ")   # always a string
age = input("Enter your age: ")     # still a string!
```

To do math with numbers from `input()`, convert them with **type casting**:

```python
age = int(input("Enter your age: "))
print("Your age is", age)
```

Other types work the same way:

```python
height = float(input("Enter your height: "))
```

### 9. Mini Practice Program

Try this program — it combines variables, `input()`, `print()`, `type()`, and type casting:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
print("Name type:", type(name))
print("Age type:", type(age))
```

## Examples Included

- Name and colour input
- Score-based grade checker
- Scholarship eligibility checker
- Even/odd number checker
- Loan eligibility checker
- Simple calculator (add, sub, mul, div)
- Multiplication table
- Number patterns with nested loops

## Author

**Archana**  
r.archanahere@gmail.com
