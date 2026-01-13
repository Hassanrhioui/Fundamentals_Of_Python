# Copyright (c) 2025 Ville Heikkiniemi

#

# This code is licensed under the MIT License.

# You are free to use, modify, and distribute this code,

# provided that the original copyright notice is retained.

#

# See LICENSE file in the project root for full license information.

# Task A – Key Notes (Python Fundamentals)

**First assignment**

# Copyright (c) 2025 Ville Heikkiniemi

#

# This code is licensed under the MIT License.

# You are free to use, modify, and distribute this code,

# provided that the original copyright notice is retained.

#

# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
Program that reads reservation details from a file
and prints them to the console:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly price: 19,95 €
Total price: 39,90 €
Paid: Yes
Location: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com
"""

## Reading a file

- Files are opened using `open()`
- `readline()` reads one line
- `strip()` removes `\n`

```python
with open("reservations.txt", "r") as file:
    line = file.readline().strip()
```
