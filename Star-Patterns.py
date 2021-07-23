# Star Patterns

# 1
for i in range(5):
    print("* " *5)

# 2
for i in range(5):
    print("* " *(i+1))

# 3
for i in range(5):
    print("  " *(5-i) +"* " *(i+1))

# 4
for i in range(5):
    print(" "*(5-i)+ "* " *(i+1))

# 5
for i in range(1,5):
    print(" "*(5-i)+ "* " *(i))
for i in range(5,0,-1):
    print(" "*(5-i)+ "* " *(i))

# 6
for i in range(5,0,-1):
    print(" "*(5-i)+ "* " *(i))

# 7
for i in range(5,0,-1):
    print("  " *(5-i) + "* " *i)

# 8
for i in range(5,0,-1):
    print("* " *i)

# 9
for i in range(1,5):
    print("* "*i)
for i in range(5,0,-1):
    print("* "*i)

# 10
for i in range(1,5):
    print("  "*(5-i) + "* "*i)
for i in range(5,0,-1):
    print("  "*(5-i) + "* "*i)

# 11
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")   #can replace j with i for differnt output
    print()

# 12
for row in range(5):
    for col in range(5):
        if col==0 or row==(5-1) or col==row:
            print("*", end="")
        else:
            print(end=" ")
    print()

# 13
n = int(input("Enter number:")) 
num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num+=1
    print()