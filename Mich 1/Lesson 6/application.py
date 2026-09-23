"""
Lesson 06 - application.py
Modules demo library imports (of calculations.py)

Easiest if files are be in the same folder

variations of import:
import calculations              # Lesson6 - slide 4
from calculations import add.    # Lesson6 - slide 5
from calculations import *.      # Lesson6 - slide 6
import calculations as calc.     # Lesson6 - slide 7

"""

import calculations

def main():
    print("hi")
print(f"{calculations.add(1.72,403.22):.2f}")
