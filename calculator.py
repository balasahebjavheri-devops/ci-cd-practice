import requests

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_random_fact():
    response = requests.get("https://catfact.ninja/fact")
    return response.json()["fact"]
