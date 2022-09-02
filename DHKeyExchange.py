import random

def generate_key(g, Ps, prime):
    
    key = ((pow(g, Ps)) % prime)
    return key

prime = int(input("Enter the prime number, P: ")) #public modulus - agreed upon by both - should be prime
generator = int(input("Enter the generator, G: ")) #public number - agreed upon by both

Person_1_Private_Secret = int(input("Enter your lone secret: ")) #private random number, picked by you
Person_2_Private_Secret = random.randint(90, 180) #your friends private random number

Person_1_Public_Key = generate_key(generator, Person_1_Private_Secret, prime) #public key established by you
print("Your public key is: " + str(Person_1_Public_Key))

Person_2_Public_Key = generate_key(generator, Person_2_Private_Secret, prime) #public key established by your friend
print("Your friends public key is: " + str(Person_2_Public_Key)) 

Shared_Secret_Person1 = generate_key(Person_2_Public_Key, Person_1_Private_Secret, prime) #secret shared by both, established by you
Shared_Secret_Person2 = generate_key(Person_1_Public_Key, Person_2_Private_Secret, prime) #secret shared by both, established by your friend

print("Secret key for A = ", str(Shared_Secret_Person1))
print("Secret key for B = ", str(Shared_Secret_Person2)) #This is for debugging purposes of course, in the real scenario nobody would know anybody else's secret key

