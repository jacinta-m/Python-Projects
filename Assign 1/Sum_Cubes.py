#    A program to find the sum of the cubes of the first n natural numbers

def cube(x):
    return x * x * x

def main():
     print("This program calculates the sum of cubes to the number n")
     a = eval(input("Please enter a number for n: "))
     sum = 0
     for number in range(1,a+1):
          sum = sum + cube(number)
     print("The sum of the nth cube is: ", sum)

main()
