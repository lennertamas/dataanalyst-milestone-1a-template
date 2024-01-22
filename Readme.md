### Exercise 1: Find the Maximum Element

Write a Python function to find the maximum element in a list of numbers without using the built-in `max()` function. If the input list is None or it is empty list, the return value must be None.

Requirements:
- Returns greatest element of a list of numbers
- In case of None input returns None
- In case of Empty input string, returns None

This excercise is measure basic python algorithmic knowledge.

### Exercise 2: Character Frequency Counter

Write a Python function that takes a string as input and counts the frequency of each character in the string. The function should return the character frequencies in a dictionary where keys should be the characters of input string and values represent the number of occurences of each characters.

Requirements:
- Returns number of umber of occurences of each characters in a dictionary like in the following sample:
    {'a': 1, 'b': 2, 'c':3}
- In case of None input returns None
- In case of Empty input string, returns None
- Space characters are removed from output

In this exercise, the function `character_frequency_counter` takes a string as input, counts the frequency of each character, and then returns the character frequencies. You can replace the `sample_string` with any string you'd like to test.

This exercise covers string manipulation and dictionary usage. 

### Exercise 3: Sql handler

Write a function that is able to connect to a database and read data from a specified table. The excercise has an sql attachment with a complext sql script for creating database for pizza ordering. Run this script on your any database to create test tables. 

Your task is wrinting code to connect this database and read all records  from pizza table.

Requirements:
- Returns every record from pizza table of attached database