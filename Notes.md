# Task A – Key Notes (Python Fundamentals)

## Reading a file

- Files are opened using `open()`
- `readline()` reads one line
- `strip()` removes `\n`

```python
with open("reservations.txt", "r") as file:
    line = file.readline().strip()
```
