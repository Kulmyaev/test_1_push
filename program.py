from typing import List

# функция
def hello():
    print("Hello world")

hello()

# Аннотация переменных
def focus(name: str,sity: str):
    print(f" {name} or {sity} ")

name: str = 'Jak'
sity: str = 'Gamora'

focus(name,sity)

name: str = 'Tommy'
age: int = 24
height_in_meters: float = 1.7
colleagues: List[str] = ['Alicia', 'John']
