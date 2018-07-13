import random
import string

def gen_prime():
## read from file prime numbers 
    line = open("largeprimes.txt","r").readlines()
    ran = random.randrange(0,len(line))
    ran2 = random.randrange(1,len(line))
    p = eval(line[ran])
    q = eval (line[ran2])
    while p==q:
            q = eval(line[ran2])
    return p,q

def gcd(a,b):
    while b!= 0:
        a,b = b, a%b
    return a

def extendgcd(e,phi):
    x, lastx, y , lasty = 0,1,1,0
    while phi !=0:
        q = e//phi
        e, phi = phi, e%phi
        x, lastx = lastx - q*x, x
        y, lasty = lasty - q*y, y
    return lastx

# function to calculate d
def inverse(e,phi):
    x = extendgcd(e,phi)
    if  x <0:
      return x+phi
    return x

# function to generate a pair of public and private keys
def keys(): 
    p, q = gen_prime()
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1,phi)
    g = gcd(e, phi)
    while g != 1:
         e = random.randrange(1,phi)
         g = gcd(e, phi)

    d = inverse(e,phi)
# writing the generated public and private keys to a file    
    file = open("testf.txt","a")
    file.write("keys:"+",")
    file.write(str(n)+",")
    file.write(str(e)+",")
    file.write(str(n)+",")
    file.write(str(d))
    file.write("\n")
    file.close
    return ((n,e),(n,d))

def encrypt(raw_msg, user_key):
    n, e = user_key
    number_msg = []
    encryption = []
    for ch in raw_msg:
        number_msg.append(ord(ch))
    for i in number_msg:
        encryption.append((i**e)%n)
    return encryption

def decrypt(input_msg, private_key):
    n, d = private_key
    msg = input_msg
    num_message =[]
    message =[]
    d_msg=""
    for i in msg.split(','):
        num_message.append(eval(i))
    for j in num_message: 
        message.append((j**d)%n)
    for st in message:
        d_msg = d_msg + chr(st)
    return d_msg    

def main():
    print ("This program encrypts or decrypts messages")
    public_key, private_key = keys()
    print ("This programs public key (n,e) is ", public_key)
    while 1:
        while 1:
            print("Please enter 'G' if you would like generate the keys ")
            print("Please enter 'E' if you would like to encrpt a message ")
            print("Please enter 'D' if you would like to decrypt a message ")
            choice = input("or type Q to quit :",)    
            if (choice[0]== "d" or choice[0]=="D" or choice [0]=="e" or choice[0]== "E"):
                break
            if (choice[0]=='g' or choice[0]=='G'):
                break
            if (choice[0] =='Q' or choice[0]== 'q'):
                break
      
        if (choice[0]=='Q' or choice[0]=="q"):
              break
        if (choice[0]=='G' or choice[0]=='g'):
            public_key, private_key = keys()    
            print ("The new public key is ", public_key," new private key is ", private_key)
    
        elif (choice[0]=="e" or choice[0]=="E"):
           raw_msg = input("Please enter your message to be encrypted :")
           print (raw_msg)
           print("Please enter the public key (n,e)for the message to be encrypted by ")
           user_n = int(input("Please enter the n ..." ))
           user_e = int(input("Please enter the e..."))           
           user_key = (user_n,user_e)
           print(user_key)
           encrypt_message = encrypt(raw_msg, user_key)
           print("Your encrypted message is :", encrypt_message)

        elif (choice[0]=="d" or choice[0]=="D"):
            input_msg = input("Please enter the message to be decrypted, numbers seperated by a comma :",)          
            print ("Please enter 1 if you wish to use this programs decryption key")
            d_choice = int(input("or 2 if you would like to input the key from the file...",))
            if (d_choice==1):
                decrypted_message = decrypt(input_msg, private_key)
                print ("Your decrypted message is ...: " ,decrypted_message)
            elif (d_choice ==2):
# reading in the private key from a file of saved key pairs
                infile = open("testf.txt","r")
                data = infile.readlines()
                line_n= int(input("Which number line is the key on..?",))
                counter = line_n - 1
                line_key = data[counter]
                new_line = ""
                keyline = ""
                for line in line_key[0:-1]:
                    new_line = new_line + line
                    keyline = new_line.split(',')
                n = eval((keyline[1]))
                e = eval((keyline[2]))
                d = eval((keyline[4]))
                sprivate_key = (n,d)
                decrypted_message = decrypt(input_msg, sprivate_key)
                print ("Your decrypted message is ...: " ,decrypted_message)
            else:
                print("Error...you did not enter a correct value")
        else:
            print("There is an error")
main() 
