#Return the sum of two numbers

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

#Raw
print('Raw method--------------------')
print('Sum of {} and {} = {}'.format(num1,num2,num1+num2))

#Function
print('Function method--------------------')

def find_sum(n1,n2):
    return n1+n2

print('Sum of {} and {} = {}'.format(num1,num2,find_sum(num1,num2)))

#OOP
print('OOP method--------------------')

class SumOfTwoNumbers:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def find_sum(self):
        return self.n1+self.n2

sotn = SumOfTwoNumbers(num1,num2)

print('Sum of {} and {} = {}'.format(num1,num2,sotn.find_sum()))