a = {"name": "Ed"}
age = input("Enter ur age: ")
name = ""

try:
    age = int(age) + 1
    print("Code after exception")
except ValueError:
    age = 18
except KeyError:
    name = "Default"
except Exception as exc:
    print(exc, type(exc))

print(f'Hello. {name}. Your age is {age}')