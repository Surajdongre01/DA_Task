# list from 1 to 50

# l1 = list(range(1,50,2))

# print(l1)

# for val in l1:
#     print(val)


buyfruit = []

lfruit = ['banana','mango','grapes','pineapple','watermelon',
          'orange','apple','avacado','dragonfruit','chiku','Anaar']

print(f'(lfruit) = {lfruit}')
print()
buyfruit.append('banana')

print()
print(f'(buyfruit) = {buyfruit}')

buyfruit.append(lfruit[2])

print()
print(f'(buyfruit) = {buyfruit}')


# banana, avacado, chiku

fbuyfruit = []
notbuy = [];
for fr in lfruit:
    print(f'fr = {fr}')
    if fr == 'banana':
        fbuyfruit.append(fr)
    elif fr == 'avacado':
        fbuyfruit.append(fr)
    elif fr == 'chiku':
        fbuyfruit.append(fr)
    else:
       # print(f'fruit = {fr} was not added')  
       notbuy.append(fr) 

print()

print(f'fbuyfruit = {fbuyfruit}')        

print()

print(f'notbuy = {notbuy}')
print()
print()

## While loop 


flength = len(lfruit)
print(flength)

print()
print()
flength = len(lfruit)

i = 1
while i <= flength:
    print(i)
    i += 1

print()
flength = len(lfruit)

i = 0
while i < flength:
    print(lfruit[i])
    i += 1    

whilefruit = []

i = 0
while i < flength:
    print()
    print(lfruit[i])
    print()
    if(lfruit[i] == 'banana'):
        (whilefruit.append(lfruit[i]))
        break
    if(lfruit[i] == 'chiku'):
        (whilefruit.append(lfruit[i]))
        break
    i += 1 
print()
print(f'whilefruit = {whilefruit}')   
