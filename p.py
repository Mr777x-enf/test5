
# Buggy Python Code - 100 Lines
# Intentionally contains multiple detectable bugs

import math
import json

# Bug 1: Undefined variable
def greet_user(name):
    print("Hello", username)

# Bug 2: Missing return statement
def add_numbers(a, b):
    result = a + b

# Bug 3: Incorrect data type
def multiply(a, b):
    return a * "2"

# Bug 4: Division by zero
def divide(a, b):
    return a / 0

# Bug 5: Wrong comparison operator
def is_adult(age):
    return age < 18

# Bug 6: Undefined variable
def calculate_square(n):
    return number * number

# Bug 7: Incorrect loop range
def print_numbers(n):
    for i in range(1, n):
        print(i)

# Bug 8: List index out of range
def get_last_element(items):
    return items[len(items)]

# Bug 9: Modifying list while iterating
def remove_even_numbers(nums):
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
    return nums

# Bug 10: Incorrect default argument
def append_item(item, items=[]):
    items.append(item)
    return items

# Bug 11: Incorrect string method
def uppercase_text(text):
    return text.uppercase()

# Bug 12: Missing argument
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100)

# Bug 13: Incorrect indentation
def check_positive(n):
    if n > 0:
    print("Positive")

# Bug 14: Undefined function
def process_data(data):
    return clean_data(data)

# Bug 15: Wrong variable used
def find_max(a, b):
    if a > b:
        return b
    return a

# Bug 16: Incorrect condition
def is_even(n):
    return n % 2 == 1

# Bug 17: Type error
def concatenate(a, b):
    return a + b

result = concatenate("Age: ", 25)

# Bug 18: Incorrect dictionary key
def get_user(users, user_id):
    return users["username"]

# Bug 19: Infinite recursion
def countdown(n):
    if n == 0:
        return
    countdown(n)

# Bug 20: Incorrect mathematical formula
def circle_area(radius):
    return 2 * math.pi * radius

# Bug 21: Undefined variable
def calculate_discount(price):
    return price - discount

# Bug 22: Incorrect list initialization
numbers = list(5)

# Bug 23: Wrong loop condition
def count_to_ten():
    i = 0
    while i < 10:
        print(i)
        i -= 1

# Bug 24: Incorrect sorting
def sort_numbers(nums):
    return nums.sort()

# Bug 25: Incorrect type conversion
def convert_to_int(value):
    return int("hello")

# Bug 26: Incorrect exception handling
def safe_division(a, b):
    try:
        return a / b
    except ValueError:
        return None

# Bug 27: Incorrect file mode
def write_file():
    file = open("data.txt", "r")
    file.write("Hello World")
    file.close()

# Bug 28: Incorrect JSON parsing
def parse_json(data):
    return json.loads(data["name"])

# Bug 29: Wrong list method
def add_element(items, element):
    return items.add(element)

# Bug 30: Incorrect return logic
def get_minimum(a, b):
    if a < b:
        return a
    return a

# Bug 31: Missing colon
def check_age(age)
    if age >= 18:
        print("Adult")

# Bug 32: Incorrect variable scope
def update_counter():
    counter += 1

counter = 0

# Bug 33: Incorrect string indexing
def first_character(text):
    return text[1]

# Bug 34: Wrong boolean condition
def validate_password(password):
    return len(password) < 8

# Bug 35: Incorrect dictionary access
def get_email(user):
    return user.email

# Bug 36: Incorrect function call
def greet(name):
    return "Hello " + name

message = greet()

# Bug 37: Incorrect factorial logic
def factorial(n):
    result = 0
    for i in range(1, n + 1):
        result *= i
    return result

# Bug 38: Incorrect list comprehension
squares = [x * x for x in range(10) if x > 10]

# Bug 39: Wrong equality check
def compare_values(a, b):
    return a = b

# Bug 40: Missing import
def calculate_root(n):
    return sqrt(n)

# Bug 41: Incorrect tuple unpacking
a, b, c = (1, 2)

# Bug 42: Wrong dictionary initialization
user = {"name": "Nitish", "age": 22}
user["email"] = user["phone"]

# Bug 43: Incorrect recursion base case
def sum_recursive(n):
    if n == 1:
        return 1
    return n + sum_recursive(n + 1)

# Bug 44: Incorrect set operation
def unique_items(items):
    return items.unique()

# Bug 45: Incorrect file handling
def read_file():
    file = open("missing.txt", "r")
    return file.read()

# Bug 46: Wrong comparison
def is_zero(n):
    return n != 0

# Bug 47: Incorrect dictionary iteration
def print_users(users):
    for key, value in users:
        print(key, value)

# Bug 48: Incorrect list concatenation
def merge_lists(a, b):
    return a - b

# Bug 49: Undefined variable
def calculate_average(nums):
    return sum(nums) / count

# Bug 50: Wrong modulo operation
def is_multiple_of_five(n):
    return n % 5 == 1

# Bug 51: Incorrect while loop
def print_reverse(n):
    while n > 0:
        print(n)
        n += 1

# Bug 52: Incorrect string formatting
def introduce(name, age):
    return "My name is {name} and I am {age}"

# Bug 53: Incorrect function return
def get_length(items):
    print(len(items))

# Bug 54: Wrong list slicing
def reverse_list(items):
    return items[1:]

# Bug 55: Incorrect logical operator
def eligible(age, income):
    return age >= 18 or income > 50000

# Bug 56: Incorrect type checking
def validate_number(n):
    return isinstance(n, str)

# Bug 57: Incorrect dictionary deletion
def remove_user(users, user_id):
    del users[user_id]
    return users

# Bug 58: Incorrect exponentiation
def power(a, b):
    return a ^ b

# Bug 59: Incorrect loop variable
def print_items(items):
    for i in range(len(items)):
        print(items[len(items)])

# Bug 60: Wrong function name
def calculate_sum(nums):
    return summ(nums)

# Bug 61: Incorrect string splitting
def get_words(sentence):
    return sentence.split(" ")

# Bug 62: Incorrect list comparison
def lists_equal(a, b):
    return a is b

# Bug 63: Incorrect exception type
def get_number(value):
    try:
        return int(value)
    except IndexError:
        return -1

# Bug 64: Wrong mathematical operation
def percentage(value, total):
    return value / total * 1000

# Bug 65: Incorrect dictionary update
def update_user(user, name):
    user.update(name)

# Bug 66: Incorrect range
def print_even_numbers():
    for i in range(2, 20, 1):
        print(i)

# Bug 67: Incorrect function argument
def area(length, width):
    return length * width

rectangle_area = area(10)

# Bug 68: Wrong condition
def check_range(n):
    return n > 10 and n < 5

# Bug 69: Incorrect list removal
def remove_item(items, value):
    items.remove(100)
    return items

# Bug 70: Incorrect string comparison
def check_admin(role):
    return role is "admin"

# Bug 71: Wrong sorting logic
def descending(nums):
    return sorted(nums)

# Bug 72: Incorrect dictionary key check
def has_name(user):
    return user.get("name") == None

# Bug 73: Wrong mathematical calculation
def average(a, b, c):
    return a + b + c / 3

# Bug 74: Incorrect Boolean return
def has_items(items):
    return len(items) < 0

# Bug 75: Wrong list indexing
def middle_element(items):
    return items[len(items) // 2 + 1]

# Bug 76: Incorrect exception handling
def get_item(items, index):
    try:
        return items[index]
    except ValueError:
        return None

# Bug 77: Incorrect string concatenation
def full_name(first, last):
    return first + last

# Bug 78: Incorrect recursive return
def fibonacci(n):
    if n <= 1:
        return n
    fibonacci(n - 1) + fibonacci(n - 2)

# Bug 79: Wrong loop initialization
def sum_numbers(n):
    total = 1
    for i in range(n):
        total += i
    return total

# Bug 80: Incorrect condition
def is_leap_year(year):
    return year % 4 != 0

# Bug 81: Incorrect dictionary value
def user_age(user):
    return user["ages"]

# Bug 82: Incorrect list extension
def extend_list(a, b):
    return a.append(b)

# Bug 83: Incorrect function call
def square(n):
    return n * n

result = square("five")

# Bug 84: Incorrect arithmetic
def subtract(a, b):
    return b - a

# Bug 85: Incorrect loop boundary
def find_item(items, target):
    for i in range(1, len(items)):
        if items[i] == target:
            return i
    return -1

# Bug 86: Incorrect string length check
def validate_username(username):
    return len(username) > 3 and len(username) < 3

# Bug 87: Wrong dictionary method
def get_keys(data):
    return data.get_keys()

# Bug 88: Incorrect comparison
def is_negative(n):
    return n > 0

# Bug 89: Incorrect list initialization
def create_matrix(rows, cols):
    matrix = [[0] * rows] * cols
    return matrix

# Bug 90: Wrong return statement
def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return False
    return True

# Bug 91: Incorrect type conversion
def convert_float(value):
    return float(None)

# Bug 92: Incorrect loop
def print_multiples(n):
    for i in range(1, 10):
        print(n * i + 1)

# Bug 93: Incorrect string replacement
def clean_text(text):
    return text.replace(" ", "")

# Bug 94: Incorrect set membership
def contains_item(items, target):
    return target not in items

# Bug 95: Incorrect condition
def check_score(score):
    if score > 100:
        return "Pass"
    return "Fail"

# Bug 96: Incorrect dictionary assignment
def create_user(name, age):
    return {"name": name, "age": age, "active": "True"}

# Bug 97: Incorrect recursion
def power_of_two(n):
    if n == 0:
        return 1
    return 2 * power_of_two(n + 1)

# Bug 98: Wrong list operation
def get_unique(nums):
    return list(set(nums)).sort()

# Bug 99: Incorrect mathematical formula
def simple_interest(p, r, t):
    return p * r * t

# Bug 100: Syntax error
def finish_program():
    print("Program completed"
