n = int(input("Enter a number for its multiplication table (e.g., 7): "))
for i in range(1, 13):
    print("{",n,"}","x","{",i,"}"," = ",n*i)
print() 

#part2
print("12x12 Multiplication Table:")
for i  in range (1,13): 
    for j in range (1,13): 
        print(i*j,end=" ")
    print()

