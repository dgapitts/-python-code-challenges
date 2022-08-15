### Python sorting algorithm 

### Problem descriptiom - sorting array input - sort case-insensitive but preserve-case in final output


Write a Python function, to sort the words in a string: 
* It should accept a string containing one or more words, separated by spaces as the input argument, and then return a string containing those words sorted alphabetically. 
* You should ignore the case of the words when sorting them. However, the output should have the same upper and lower case letters as the corresponding input words. 
* For example, the input string, banana, ORANGE apple, should produce the output shown here with apple banana, ORANGE. Notice that even though the word orange was capitalized, it was still sorted to the end of the output string because that's where it belongs alphabetically. 


### My solution

Reviewing the [python docs for sorted](https://docs.python.org/3/howto/sorting.html) made this challenge very easy: 

```
~/projects/python-code-challenges $ cat docs/sort-case-insensitive-preserve-case.py

## https://docs.python.org/3/howto/sorting.html
def sort_case_insensitive_preserve_case(input_phrase):
  print(sorted(input_phrase.split(), key=str.lower))

sort_case_insensitive_preserve_case("This is a test string from Andrew")
sort_case_insensitive_preserve_case("apple banana ORANGE")
sort_case_insensitive_preserve_case("apple ORANGE Banana ")
```


and running this
```
~/projects/python-code-challenges $ /usr/local/opt/python@3.9/bin/python3.9 /Users/dave/projects/python-code-challenges/docs/sort-case-insensitive-preserve-case.py
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
['apple', 'banana', 'ORANGE']
['apple', 'Banana', 'ORANGE']
```