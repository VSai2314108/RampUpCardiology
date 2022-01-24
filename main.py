#r
from random import randint
alpha = ['0', '1', '2', '3', '4' , '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#print(numeric0)
numeric0 = []
for y in range(36):
    numeric0.insert(randint(0,len(numeric0)),y)
#print(alpha)
hard = ['a', 'b', 'c', 'f', 'e', 'd', 'g', 'h', 'i', 'l', 'k', 'j', 'm', 'n', 'o', 'r', 'q', 'p',
        's', 't', 'u', 'x', 'w', 'v', 'z', 'y', '9', '0', '8', '1', '7', '2', '6', '3', '5', '4']
#print(hard)
numeric1 = []
for y in range(36):
    numeric1.insert(randint(0,len(numeric1)),y)
#pirnt(numeric)
soft = []
for x in alpha:
    soft.insert(randint(0,len(soft)),x)
print(soft)
def decode(valin):
    output = ""
    for x in valin:
        if(x == ' '):
            output = output + x;
        else:
            in0 = soft.index(x)
            in1 = numeric1.index(in0)
            in2 = alpha[in1]
            in3 = hard.index(in2)
            in4 = numeric0.index(in3)
            output = output + alpha[in4]
    return output

def encode(valin):
    output = ""
    for x in valin:
        if(x == ' '):
            output = output + x
        else:
            in0 = alpha.index(x)
            in1 = numeric0[in0]
            in2 = hard[in1]
            in3 = alpha.index(in2)
            in4 = numeric1[in3]
            output = output + soft[in4]
    return output

def shuffle():
    soft.clear()
    for x in alpha:
        soft.insert(randint(0,len(soft)),x)
    numeric0.clear()
    for y in range(36):
        numeric0.insert(randint(0,len(numeric0)),y)
    numeric1.clear()
    for y in range(36):
        numeric1.insert(randint(0,len(numeric1)),y)
    print(soft)
    
def main():
    command = input("Enter decode, encode, shuffle, or any other character to exit the function: ")
    if command=="decode":
        passin = input("Enter string with letters, numbers, and spaces: ")
        print (decode(passin))
        main()
    elif command=="encode":
        passin = input ("Enter string with letters, numbers, and spaces: ")
        print (encode(passin))
        main()
    elif command=="shuffle":
        shuffle()
        main()
    else:
        pass
    
    
main()
        
        

            
            
        
        
        
    


    

    

