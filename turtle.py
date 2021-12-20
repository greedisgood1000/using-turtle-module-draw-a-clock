#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle   as tu
import math    
import datetime as dt
import random   as rd
import time

#回到初始位置
def initial():
 tu.penup()
 tu.home()
 tu.pendown()
 tu.pensize(1)
 tu.pencolor("black")
 tu.tracer(False)

#表盘及刻度
def clock_carrier():
 initial()
 tu.tracer(False)
 tu.left(90)
 tu.penup()
 tu.forward(d)
 tu.left(90)
 tu.pendown()
 tu.begin_fill()
 tu.circle(d)
 tu.end_fill()
 for i in range(1,13):
  initial()
  tu.tracer(False)
  tu.penup()
  tu.left(float((i-1)*30))
  tu.forward(d/1.3)
  tu.pendown()
  tu.pensize(5)
  tu.forward(d/25)
  tu.penup()
  tu.left(i)
  tu.pendown()
  a=(-i+4)%12 if ((-i+4)%12)!=0 else '12'
  tu.write(a,align="center",font=("宋体",int(d/15)))
 for j in range(61):
  initial()
  tu.tracer(False)
  tu.penup()
  tu.left(float(j*6))
  tu.forward(d/1.3)
  tu.pendown()
  tu.pensize(2)
  tu.forward(d/25)
  
#导入时间
def timing():
 initial()
 global hours,minutes,seconds,today_data,time_now
 data=dt.datetime.now().strftime("%Y.%m.%d.%H.%M.%S").split('.')
 today_data='{}年{}月{}日'.format(data[0],data[1],data[2])
 time_now='{}时{}分{}秒'.format(data[3],data[4],data[5])

 t=dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S").split('-')
 hour,minute,second=int(format(t[3])),int(format(t[4])),int(format(t[5]))
 hours=float(hour+minute/60+second/3600)
 minutes=float(minute+second/60)
 seconds=float(second)

#时针
def hour():
 initial()
 tu.pensize(10)
 tu.right((hours-3)*30)
 tu.forward(d/2.8)

#分针
def minute():
 initial()
 tu.pensize(4)
 tu.right((minutes-15)*6)
 tu.forward(d/1.8)

#秒针
def second():
 initial()
 tu.pensize(1)
 tu.right((seconds-15)*6)
 tu.forward(d/1.5)
 
#日期和时间
def data(data1,data2):
 initial()
 tu.right(90)
 tu.penup()
 tu.forward(0.3*d)
 tu.pendown()
 tu.write(data1,align="center",font=("宋体",int(d/20),"bold"))
 
 initial()
 tu.right(90)
 tu.penup()
 tu.forward(0.4*d)
 tu.pendown()
 tu.write(data2,align="center",font=("宋体",int(d/20),"bold"))
 
#main
def main():
 timing()
 tu.getscreen()
 hour()
 minute()
 second()
 data(today_data,time_now)
 
 
d=float(input("please input the diameter of clock(100~230):"))
tu.fillcolor(rd.random(),rd.random(),rd.random())
while 1==1:
    clock_carrier()
    main()
    time.sleep(1)
    tu.clear()




# In[ ]:




