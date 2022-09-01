'''Loops'''
I = int(input("Enter the number"))
while I>0:
    print("Hello")
    I = I-1

for loop in range(5):
    print(8)
    I = I-1

# for loops with else
l = [ 1, 7, 8]
for item in l:
    print(item)
    print("Done")

#Break
for i in range(0, 80):
    print(i)
    if i == 3:
        break

#Cntinue
for i in range(0, 8):
    print(i)
    if i == 3:
        break
