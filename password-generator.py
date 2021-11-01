import string 
import random

if __name__ == '__main__':
    
    s1= string.ascii_lowercase
    s2= string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    try:
        plen=int(input("enter password length :\n"))
    except:
        print("not an integer")
        exit()
    try:
        if plen>20:
            print(invalid)
    except:
        print("enter smaller value")
        exit()            
     
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("your password:")
    print("".join(random.sample(s,plen)))
     
        
     
      
     
     
     
