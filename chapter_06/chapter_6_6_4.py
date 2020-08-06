# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with ía loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

valdict = {
    "variable": "Elementar data type that stores values",
    "loop": "Self repeating structure",
    "dictionary": "Glossary structure",
    "array": "List of elements",
    "conditional": "Conditional test",
    "word0": "Value0",
    "word1": "Value1",
    "word2": "Value2",
    "word3": "Value3",
    "word4": "Value4"
}

for key in valdict:
    print(key + ", " + valdict[key])