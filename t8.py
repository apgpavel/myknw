def pdecorate(f):
   def func_wrapper(*args):
       return 'Декорирование вывода {0}'.format(f(*args))
   return func_wrapper

class Complex:

    def __init__(self, a, b):
        '''Init класса'''
        self.a = a
        self.b = b

    def __str__(self):
        '''Вывод числа в формате str'''
        return '(%s, %s)' % (self.a, self.b)


    def __add__(self, other):
        '''Операция сложения'''
        com_a = self.a + other.a
        com_b = self.b + other.b
        return Complex(com_a, com_b)

    def __sub__(self, other):
        '''Операция вычетания'''
        com_a = self.a - other.a
        com_b = self.b - other.b
        return Complex(com_a, com_b)

    def __mul__(self, other):
        '''Операция умножения'''
        com_a = self.a * other.a - self.b * other.b
        com_b = self.a * other.b + self.b * other.a
        return Complex(com_a, com_b)

    @pdecorate
    def __truediv__(self, other):
        '''Операция деления'''
        com_a = round((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2), 2)
        com_b = round((self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2), 2)
        return Complex(com_a, com_b)

i1 = Complex(1, 2)
i2 = Complex(2, 5)

i3 = i1 + i2
i4 = i1 - i2
i5 = i1 * i2
i6 = i1 / i2
print(i3)
print(i4)
print(i5)
print(i6)
