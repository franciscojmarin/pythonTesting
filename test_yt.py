import requests

name = input("Your name? ")
print("Hello, ", name)
print("Hello, Word!")
print("Desde la rama")
print("Desde la ramaRama")

r = requests.get("https://coreyms.com")
print(r.status_code)
