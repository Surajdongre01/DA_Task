people = [{"name": "jon snow","age": 28},
           {"name": "robb stark","age": 25},
           {"name": "sansa stark","age": 19},
           {"name": "arya stark","age": 17},
           {"name": "bran stark","age": 14}]

print(f'people = {people}')
print()

# while loop

index = 0 
while index < len(people):
    print(people[index]["name"])
    index += 1
print()

# for loop 

ages = []
for person in people:
    ages.append(person["age"])
    print(f'ages = {ages}')
print()



# Map

names = list(map(lambda person: person["name"],people))
print(f'names = {names}')
print()


# filter

older_than_19 = list(filter(lambda person: person['age'] >= 19, people))
print(f'older_than_19 = {older_than_19}')

