# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
# Your code here

string = "Python Programming"
result =string [::-1]
print(result)

# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
# Your code here

string = "racecar"
if string == string[::-1]:
  print("palindrome")
else:
  ("not a palindrome")

# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
# Your code here

x = "Python is a great programming language"
total_words = len(x.split())
print(total_words)

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
# Your code here
x =  "hello world"
result = x.title()
print(result)

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
# Your code here
string = "Data Science"
length = len(string)
print(length)

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
# Your code here
x = "Machine Learning"
result = x.replace(" ","_")
print(result)

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
# Your code here
text = "Python Programming Language"
if "python" in text:
  print("python is pracent")
else:
  print("python is not pracent")

# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
# Your code here
text = "Artificial Intelligence"
extract = text[:5]
print(extract)

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
# Your code here
text = "UPPERCASE"
result = text.lower()
print(result)

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
# Your code here
text = "Computer Science"
result = text.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(result)

# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
# Your code here
text = "mississippi"
result = max(text,key=text.count)
print(result)

# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
# Your code here
a = "listen"
b = "silent"
c = len(a)
d = len(b)
print(sorted(a))
print(sorted(b))
if sorted(a) == sorted(b):
  print("anagrams")
else:
  print("not anagrams")

# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
# Your code here
text = "python programming language"
result = text.title()
print(result)

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
# Your code here
text = "Hello World"
count = 0
for i in text:
  if i !=" " and i not in ("aeiou"):
    count+=1
print(count)

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
# Your code here
text = "Python is a programming language"
words = text.split()
result = max(words)
print(result)

# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
# Your code here
string = "Hello, World! How are you?"
result = string.replace(",","").replace("!","").replace("?","")
print(result)

# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
# Your code here
string = "Python is easy to learn"
if string.startswith("Python"):
  print("yes")
else:
  print("No")

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
# Your code here
text = "Hello World"
result = text.index("o")
print(result)

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
# Your code here
fruits = "apple,banana,orange"
result = fruits.split(",")
print(result)

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
# Your code here
text = ['Python', 'is', 'awesome']
result = " ".join(text)
print(result)

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here
string = "12345"
if string.isdigit():
  print("only digit")
else:
  print("not only digit")

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here
string = "HelloWorld"
if string.isalpha():
  print("only letters")
else:
  print("not only letters")

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here
string =  "banana"
for i in range(len(string)):
  if string[i] == "a":
    print(i)

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here
text = "  Hello World  "
result = text.strip()
print(result)

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here
string = "programming"
if string.endswith("ing"):
  print("condition is true")
else:
  ("condition is false")

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here
text = "Hello World"
replace = text.replace("o","0",1)
print(replace)

# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# Your code here
string ="Python is a programming language"
result = min(string.split(),key = len)
print(result)

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here
text = "Python programming is powerful"
result = text.count("p")
print(result)

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here
text = "Hello World Python"
result = text.split()
word = " ".join(result[::-1])
print(word)

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here
string = "user@example.com"
if "@" in string and "." in string:
  print("valid email format")
else:
  print("invalid email fomat")

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here
url = "https://www.example.com/path"
result = url.split("/")[2]
print(result)

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here
text = '''hello python and
data engineer and
data science and
machine learning'''
result = text.splitlines()
length = len(result)
print(length)

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here
text1 = "hello"
text2 = "world"
result = set(text1) & set(text2)
print(result)

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
# Your code here
text = "abc123def456ghi789"
result = ""
for char in text:
  if char.isdigit():
    result += char
print(result)

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here
text = "snake_case"
result = text.replace("_c","C")
print(result)

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here
string = "A man a plan a canal Panama"
text = string.replace(" ","")
result = text.lower()
if result == result[::-1]:
  print("string is palindrome")
else:
  print("string is not a palindrome")

# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here
text = "the quick brown fox jumps over the lazy dog"
result = text.split()
word = max(result)
print(word)

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here
text = "National Aeronautics and Space Administration"
word = text.split()
result = ""
for i in word:
  result += i[0]
print(result)

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here
string = "((()))"
if string == " " and string == ():
  print("x")
else:
  print("y")

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here
url = "https://www.google.com"
if url.startswith("https://") or url.startswith("http://"):
  print("valid URL")
else:
  print("in valid URL")

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here
string = "Python programming is amazing and powerful"
words = string.split()
result = []
for i in words:
  if len(i)>5:
    result.append(i)
print(result)

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here
text = "hello world"
word = text.split()
result=[]
for i in word:
  new_word = i[1:] + i[0] + "ay"
  result.append(new_word)
print(" ".join(result))

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here
ip = "192.168.1.1"
result = ip.split()
if len(result)==4 and all(0 <= int(x) <= 255 for x in result):
  print("valid IPv4")
else:
  print("invalid IPv4")

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here
text = "abc"

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        print(text[i:j])

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here
import codecs

text = "hello world"

result = codecs.encode(text, "rot_13")

print(result)

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 
card = "4532015112830366"
if len(card) == 16:
  print("valid credit card")
else:
  print("invalid credit card")
