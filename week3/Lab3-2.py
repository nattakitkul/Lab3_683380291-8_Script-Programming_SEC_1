#part1
n = int(input("Enter a number : "))
while n > 0:
    print(n)
    n-=1
print("Blast off!")

#part2
sec=42
t=0
heart=5
while t!=sec :
    t = int(input("Guess the number: "))
    if(heart<0):
        print("You Fail")
        break
    if(t>sec):
        print("Too high! Try again.")
        heart-=1
    elif(t<sec):
        print("Too low! Try again.")
        heart-=1
    elif(t==sec): 
        print("Congratulations! You guessed it!")
