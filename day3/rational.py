import random
from sorts import *

class Rational():
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    ######################## MATH FUNCTIONS ########################
    def __mul__(self,other):
        rational = Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        rational.simplify()
        return rational

    def __truediv__(self,other):
        other.numerator,other.denominator = other.denominator,other.numerator
        return self * other

    def __floordiv__(self,other):
        return self/other

    def __add__(self,other):
        if self.denominator == other.denominator:
            return Rational (self.numerator + other.numerator, self.denominator)
        least_common_denominator = self.lcd(self.denominator,other.denominator)
        self_numerator = self.numerator * (least_common_denominator // self.denominator)
        other_numerator = other.numerator * (least_common_denominator // other.denominator)
        rational = Rational(self_numerator + other_numerator, least_common_denominator)
        rational.simplify()
        return rational

    def __sub__(self,other):
        return self + -other

    def __neg__(self):
        self.numerator = -self.numerator
        return self

    #Euclidean algorithm
    def gcf(self,num1,num2):
        greater_num = max(num1,num2)
        #print(greater_num)
        lesser_num = min(num1,num2)
        #print(lesser_num)
        if greater_num % lesser_num == 0:
            return lesser_num
        return self.gcf(lesser_num, greater_num % lesser_num)

    def lcd(self,num1,num2):
        return (num1 * num2) // self.gcf(num1,num2)

    def simplify(self):
        isNegative = self.numerator < 0 or self.denominator < 0
        self.numerator,self.denominator = abs(self.numerator),abs(self.denominator)
        GCF = self.gcf(self.numerator, self.denominator)
        self.numerator //= GCF
        self.denominator //= GCF
        if isNegative:
            self.numerator = -self.numerator
    #####################################################

    def __lt__(self,other):
        least_common_denominator = self.lcd(self.denominator,other.denominator)
        self_numerator = self.numerator * least_common_denominator
        other_numerator = other.numerator * least_common_denominator
        return self_numerator < other_numerator

    def __gt__ (self,other):
        least_common_denominator = self.lcd(self.denominator,other.denominator)
        self_numerator = self.numerator * least_common_denominator
        other_numerator = other.numerator * least_common_denominator
        return self_numerator > other_numerator

    def __eq__(self,other):
        least_common_denominator = self.lcd(self.denominator,other.denominator)
        self_numerator = self.numerator * least_common_denominator
        other_numerator = other.numerator * least_common_denominator
        return self_numerator == other_numerator

    def __ge__(self,other):
        return self > other or self == other

    def __le__(self,other):
        return self < other or self == other

    def __str__(self):
        self.simplify()
        return str(self.numerator) + '/' + str(self.denominator)

if __name__ == '__main__':
    rat1 = Rational(3,16)
    rat2 = Rational(4,5)
    print('The product of', str(rat1),'and',str(rat2),'is:', str(rat1*rat2))
    print('The sum of', str(rat1),'and',str(rat2),'is:', str(rat1+rat2))
    print('The difference of', str(rat1),'and',str(rat2),'is:', str(rat1-rat2))
    print('The quotient of', str(rat1),'and',str(rat2),'is:', str(rat1/rat2))
    print('The current rationals:', str(rat1), str(rat2))

    numerators = [4,6,7,13,6,8,100]
    denominators = [1,5,6,2,3]
    rationals_list = []
    for i in range(5):
        rationals_list.append(Rational(random.choice(numerators), random.choice(denominators)))

    print('Printing the list of rationals:')
    for rational in rationals_list:
        print(str(rational))

    print('Sorting rationals...')
    rationals_list = merge_sort(rationals_list)
    for rational in rationals_list:
        print(str(rational))
