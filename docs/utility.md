# README

## Overview
This repository contains code that performs string comparison operations, calculates edit distances, and processes differences between two strings. The core components of the code include custom classes (`Nt`, `PropT`) for managing number lists and properties, and functions that compute string differences based on the **Levenshtein Distance** algorithm.

## Code Components

### 1. **Nt Class**
- Inherits from Python's built-in `list`.
- **Custom Operators:**
  - `__add__`: Adds an integer to all elements of the list or concatenates another list.
  - `__sub__`: Subtracts an integer from all elements of the list.
  - `__gt__`, `__lt__`, `__ge__`, `__le__`: Compares each element of the list with an integer.
  
- **Additional Methods:**
  - `process_list`: Manipulates elements of the list by adding or subtracting values based on conditions.
  - `overlap()`: Checks if there are duplicate elements in the list.
  - `calculate_Nt()`: Performs calculations on the list using operations like insert or delete.

### 2. **PropT Class**
- Manages properties such as size, weight, and italic status.
- Methods include:
  - `set()`: Set property values.
  - `get()`: Retrieve property values.
  - `copy()`: Create a copy of the `PropT` object.

### 3. **String Comparison Functions**
- `levenshtein_distance(s1, s2)`: Calculates the minimum number of edits (insertions, deletions, substitutions) required to transform string `s1` into `s2` using dynamic programming.
- `find_differences(s1, s2)`: Identifies the differences between two strings and returns a list of operations (insert, delete, replace).
- `history(s1, s2)`: Computes a list of edit operations required to transform `s1` into `s2`.
- `nhistory(s1, s2)`: Uses the `Levenshtein.opcodes` method to return a list of edit operations in a compact format.

### 4. **Markdown Conversion Function**
- `convert_to_md(text)`: Extracts URLs and text from markdown-like syntax (e.g., `(text)(url)`) using regular expressions.

## Example Usage

### String Comparison
```python
s1 = "kitten"
s2 = "sitting"
# Calculate Levenshtein distance
distance = levenshtein_distance(s1, s2)
print(distance)  # Output: 3

# Find the difference operations
differences = find_differences(s1, s2)
print(differences)  # Output: [('replace', 0, 1), ('insert', 6, 1)]
```

### Custom Nt Class
```python
nt = Nt([1, 2, 3, 4])
print(nt + 5)  # Output: [6, 7, 8, 9]
print(nt - 2)  # Output: [-1, 0, 1, 2]
print(nt.overlap())  # Output: False
```

### PropT Class
```python
pt = PropT(sz=12, wt="bold", it=True)
print(pt.get("size"))  # Output: 12
pt.set("size", 14)
print(pt)  # Output: PT('size': 14 'weight': bold 'italic': True)
```

## Dependencies
- `Levenshtein`: The code uses the `Levenshtein` package for efficient string comparison. Make sure to install it using:

```bash
pip install python-Levenshtein
```

## License
This project is licensed under the MIT License.

## Contribution
Feel free to contribute by forking the repository and submitting pull requests.

