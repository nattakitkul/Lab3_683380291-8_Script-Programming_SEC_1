
# Buggy Snippet A: Infinite Loopcounter = 0
counter = 0
while counter < 5:
    print(counter)
    counter+=1
# Buggy Snippet B: Incorrect Range
for i in range(1, 6): # Goal: print 1, 2, 3, 4, 5
    print(i)
    
# Buggy Snippet C: Misplaced Break
for char in "hello":
    print(char)
    if char == 'l':
        print("Found 'l', stopping!")  
        break
    
    