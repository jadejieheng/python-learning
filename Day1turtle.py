"""
绘制小猪佩奇
this version is like in processing.py,
which is object oriented programing
"""
from turtle import *
"""
turtle.pensize(4)
turtle.hideturtle()
turtle.colormode(255)
turtle.color((255, 155, 192), "pink")
turtle.setup(840, 500)
turtle.speed(10)
"""

def nose(x,y):# notice that here x and y are ot defined, nothing would run
    """画鼻子"""
    penup()
    # 将画笔移动到指定的坐标 pu()
    goto(x,y)
    pendown()
    #放下画笔pd()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)#seth() pen angle? 让海龟面向指定的方向
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90: #set up a loop 120 times???, or 0 to 120 degree?
            a = a + 0.08
            # 向左转3度
            left(3)
            # 前进a像素 move a pixel, a is always changing, I guess that changes the angle
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    """画头"""
    color((255, 155, 192), "pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30) # 顺时针画一个半径为300,圆心角为30°的园
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3) #向左转3度
            fd(a) #向前走a的pxiels
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x,y):
    """画耳朵"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x,y):
    """画眼睛"""
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):
    """画脸颊"""
    color((255, 155, 192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y):
    """画嘴巴"""
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def setting():
    """设置参数"""
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    """主函数"""
    setting() 
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()
    #在Python当中，如果代码写得规范一些，
    # 通常会写上一句“if __name__==’__main__:”作为程序的入口，
    # 但似乎没有这么一句代码，程序也能正常运行。with only "main()" it is able to ru
    # 这句代码多余吗？
    #_name_代表当前模块的名字,_name_不再是_main_
    #因此其中的main()不再被执行
    # 最终得到我们想要的输出
"""
import turtle
t = turtle.Pen()
t.forward()
t.left()..."""#is another way pf coding turtle? direct run, pusedo coding