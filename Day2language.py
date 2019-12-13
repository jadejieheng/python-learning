"""
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。"""

"""string"""
str1 = 'hello, world!'
print('字符串的长度是:', len(str1))#13
print('单词首字母大写: ', str1.title())#Hello, World!
print('字符串变大写: ', str1.upper())#HELLO WORLD!
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())#false
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)



"""variable"""
a = 14
b = 3

print(a + b)   #17
print(a - b)   #11
print(a * b)   #42
print(a / b)   #4.6666667
print(a // b)  #floor division 4, 3*4=12
print(a % b)   #Modulus 2, 3*4=12+2
print(a ** b)  #Exponentiation 2744 14*14*14

a = int(input('a = ')) #运行后用键盘输入
b = int(input('b = ')) #非整数用float
print('%d + %d = %d' % (a, b, a + b))#unlike print(a+b), it prints:(eg)4+4=8
print('%d - %d = %d' % (a, b, a - b))# 4 - 4 = 0
print('%d * %d = %d' % (a, b, a * b))# 是按照顺序对应括号内的
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
#其中%d是整数的占位符，%f是小数的占位符，%%表示百分号,so those ar string operation?
#'%.4f' % xxxx, muxt have quotation, 
#like print('%.1f' % 12.4535) = 12.5, %f means the original
#print('%.1f华氏度 = %.1f摄氏度' % (f, c)) = xx.0华氏度 = xx.x摄氏度

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>

a = 100
b = str(a)
c = 12.345
d = str(c)
e = '123'
f = int(e)
g = '123.456'
h = float(g)
i = False
j = str(i)
k = 'hello'
m = bool(k)
print(a)
print(type(a))#int
print(b)
print('str(a) is ', type(b))#str(a) is <class 'str'>
print(c)
print(type(c))
print(d)
print('str(c) is', type(d))
print(e)
print(type(e))
print(f)
print('int(e) is', type(f))#int, = print(type(int('123')))
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))
print(k)
print(type(k))
print(m)
print(type(m))



"""operation"""
a = 10
b = 3
a += b # 相当于：a = a + b
a *= a + 2 # 相当于：a = a * (a + 2)
print(a) # 10+3=13，13+2=15，13*15=195

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)# 4(5+10-3)/5 = 9.6




"""conditions"""
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)#true
print("flag2 = ", flag2)#flase
print("flag3 = ", flag3)#false
print("flag4 = ", flag4)#true
print("flag5 = ", flag5)#false
print(flag1 is True)#true
print(flag2 is not False)#flase


""" in ipython it is possible to run several prints"""
""" while in python, just run the last result?? """
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))#保留了一位小数，2即两位
#in not interactive python(hmm..is it?):
#>>> f = float(input('请输入华氏温度: '))
#请输入华氏温度: 12
#>>> c = (f - 32) / 1.8
#>>> print('%.1f华氏度 = %.1f摄氏度' % (f, c))#保留了一位小数，2即两位
#12.0华氏度 = -11.1摄氏度



"""different ways of import"""
import math
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.3f' % perimeter)
print('面积: %.6f' % area)

from math import *
radius = float(input('请输入圆的半径: '))
perimeter = 2 * pi * radius
area = pi * radius * radius
print('周长: %.3f' % perimeter)
print('面积: %.6f' % area)



"""lead year, conditions"""
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or \
           year % 400 == 0
#四年一闰，百年不闰，四百年再闰.
print(is_leap)

