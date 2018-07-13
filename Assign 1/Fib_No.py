#    A program that computes the nth Fibonacci number.

def main():
     print("This program calculates the Nth Fibonacci number")
     a = eval(input("Please enter a number for N: "))
     if a == 1:
         print("The Fibonacci number is: ", a)
     else:
         x = 0
         y = 1
         for number in range(1,a):
             count = x + y
             x = y
             y = count
         print("The Nth Fibonacci number is: ", count)

main()

