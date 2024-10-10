import random
import string
def generatepass(n):
    passw=string.ascii_letters + string.digits + string.punctuation
    pass1=' '.join(random.choice(passw) for c in range (n))
    return pass1
n=int(input('Enter the length of password: '))
print('password is: ', generatepass(n))
  