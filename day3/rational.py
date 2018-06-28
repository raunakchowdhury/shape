class Rational():
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self,other):
        rational = Rational(self.numerator + other.numerator, self.denominator + other.denominator)
        rational.simplify()
        return rational

    #Euclidean algorithm
    def gcf(num1,num2):
        greater_num = max(num1,num2)
        lesser_num = min(num1,num2)
        if greater_num % lesser_num == 0:
            return lesser_num
        else:
            return gcf(lesser_num, greater_num % lesser_num)

    def simplify():
        GCF = gcf(self.numerator, self.denominator)
        self.numerator /= GCF
        self.denominator /= GCF

if __name__ == '__main__':
    rat1 = Rational(3,5)
    rat2 = Rational(4,5)
    string = ''
    print(dir(string))
