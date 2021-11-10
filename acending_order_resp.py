#python 
#acending order.py
#R Sadhukhan_coding
#responsive
#.........import........
import sys
#.........input..........
a = eval(input('Enter first number:'))
b = eval(input('Enter second number:'))
c = eval(input('Enter third number:'))
#........logical_structure........
if a<b<c:
  print("Numbers in acending order : " ,a,b,c )
  sys.exit()
if a<c<b:
  print("Numbers in acending order : " ,a,c,b )
  sys.exit()
if b<a<c:
  print("Numbers in acending order : " ,b,a,c )
  sys.exit()
if b<c<a:
  print("Numbers in acending order : " ,b,c,a )
  sys.exit()
if c<a<b:
  print("Numbers in acending order : " ,c,a,b )
  sys.exit()
if c<b<a:
  print("Numbers in acending order : " ,c,b,a )
  sys.exit()
if a==b==c:
  print("Same Numbers:",a)
  