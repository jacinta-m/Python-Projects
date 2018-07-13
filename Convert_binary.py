def convert(n):
    if n<2:
       return [n] 
    else: 
        return convert(n//2) + [n%2]
    
def main ():
    n = int(input("Please enter a decimal number:",))
    print ( "The decimal number is :", n)
    print( ''.join(map(str, convert(n)))," is the binary representation")
    convert (n)
    print ("^ is the most significant figure")
main () 
    
