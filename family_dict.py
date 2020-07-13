my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}


for family_member in my_family.items():
  print(f"{family_member[1]['name']} is my {family_member[0]} and is {family_member[1]['age']} years old.")
  