# first_repository

# <h2> Table of contents
1. Spreadsheet
2. Code example
3. Text


 #<h3> Spreadsheet

 Python has a set of built-in methods that you can use on lists/arrays.
 
| Method | Description |
| ------- | ----------- |
| `append()` | 	Adds an element at the end of the list |
| `clear()` | Removes all the elements from the list |
| `copy()` | Returns a copy of the list |
| `count()` | Returns the number of elements with the specified value |
| `extend()` | Add the elements of a list (or any iterable), to the end of the current list |
| `index()"` | Returns the index of the first element with the specified value |
| `insert()` | Adds an element at the specified position|
| `pop()` | Removes the element at the specified position |
| `remove()` | 	Removes the first item with the specified value |
| `reverse()` | Reverses the order of the list |
| `sort()` | 	Sorts the list|

 #<h3> Code example
 
 ```python
 def most_freq(text_with):
    sort_text = sorted(set(text_with), key=text_with.count)
    freq = sort_text[-1]
    print(f"Most popular word: {freq}. It was seen {text_with.count(freq)} times")
    return freq
```

 #<h3> Text
 
 Lorem *ipsum* dolor _sit_ amet, __consectetur__ adipiscing elit, sed do eiusmod tempor **incididunt** ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 