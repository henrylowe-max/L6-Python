"""
Lesson 06 - calculations.py
Modules demo library
"""
def add(a:int|float ,b:int|float)-> int|float:
    return a + b
def multiply(a:int|float ,b:int|float)-> int|float:
    return a * b

def main():
    print("hello")
    
    
if __name__ == "__main__":
    print("testing...")
    print(f"add(2,3) = {add(2,3)}")