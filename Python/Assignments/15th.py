
def test(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
            
n = int(input('Enter the number: '))
for i in test(n):
    print(i,end=",")


def even_number(n):
    for i in range(n+1):
        if i%2==0:
            yield i
            
n = int(input('Enter the number: '))
for i in even_number(n):
    print(i,end=",")


def fibo(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    if n>1:
        return fibo(n-1)+fibo(n-2)

n = int(input('Enter the number'))

list1 = [fibo(i) for i in range(n+1)]
print(list1)

def get_username(email):
    email = email.split('@')
    return (f'The username is {email[0]}')

email = input('Enter the email id: ')
a = get_username(email)
print(a)


class shape():
    def area(self):
        return 0

class square(shape):

    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length**2

a = square(10)
print(a)


    


