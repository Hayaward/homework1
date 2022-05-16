
decimal = int(input('enter a decimal number'))
binary=[]
while decimal>0:
    binary.append(str(decimal%2))
    decimal//=2
binary.reverse()
print(''.join(binary))
