l1 = list(range(1,10,2))

print(f'l1 = {l1}')

# for val in l1:
#     print(val)

# sqvalue = []
# for val in l1:
#     print(f'val = {val}, square = {val* val}')
#     sqvalue.append(val*val)

# print()
# print(f'sqvalue = {sqvalue}')

print()

square = lambda x: x * x

newmapobj = list(map(square,l1))

print()

print(f'newmapobj  = {newmapobj}')

print()

# squarelist = list(newmapobj)

# print(f'squarelist = {squarelist}')

numbers = [1,2,3,4,5]
evennumbers = filter(lambda x: x % 2 == 0 ,numbers)

print(list(evennumbers))