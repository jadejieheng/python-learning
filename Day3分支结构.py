"""
用户身份验证
Author: 骆昊
"""
# import getpass 用于隐藏密码
# from getpass import getpass
# from getpass import *

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 输入口令的时候终端中没有回显,getpass模块只能用于命令行界面！^_^
# password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')


"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
Author: 骆昊
唯一需要说明的是和C/C++、Java等语言不同，Python中没有用花括号来构造代码块而是使用了缩进的方式来设置代码的层次结构，
如果if条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了，
换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体。
嵌套层次多了之后会严重的影响代码的可读性:
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))



"""
英制单位英寸和公制单位厘米互换
Author: me
"""

value = float (input('')) 
unit = input('')
if unit == 'in':
    print('%f inch = %f cm' % (value, 2.54 * value))
elif unit == 'cm':
    print('%f cm = %f inch' % (value, value / 2.54))
else: 
    print('please retry')


"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E
Author: me
"""

score = float(input('score = '))
if score >= 90:
    print('grade = A')
if score >= 80 and score <= 89:
    print('grade = B')
if 79 >= score >= 70:   #you can do consecutive
    print('grade = C')
if score >= 60:         #in fact you don't need to define the max
    print('grade = D')
if score <= 60:
    grade = 'E'  #infact, just type grade = 'E', change everthing above

print('grade =', grade)



"""
掷骰子决定做什么事情
run random results without inputs
Author: 骆昊
"""
from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)


"""
输入月收入和五险一金计算个人所得税 old
wooooooooow
Author: 骆昊
"""

salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)#absolute value
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))


"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
Author: me
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:# have to satisfy three conditions
    print('Yes, it is a triangle')
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))#海伦公式S=√p(p-a)(p-b)(p-c)
    print(('perimeter = %.2f' % (p * 2)), 'how can I put a unit')
    print ('area = %.2f' % (area))
else:
    print('It is not a triangle.')