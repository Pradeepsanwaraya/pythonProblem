# .
# 🟢 Topic 6: Mini Programs (46–60)
# Area of Circle
# Perimeter of Rectangle
# Simple Interest
# Compound Interest
# Percentage of 5 Subjects
# Celsius to Fahrenheit
# Fahrenheit to Celsius
# Kilometer to Meter
# Meter to Kilometer
# Seconds to Hours-Minutes-Seconds
# Gross Salary
# Electricity Bill (Basic Formula)
# Discount Calculator
# Profit & Loss
# BMI Calculator  




r=20
area=3.14*r*r
print(area)
#parameter of rectangle
l,b=10,20
print(2*(l+b))
#simple interest
p,rt,t=1000,2,5
si=(p*rt*t)/100
print(si)  
#compound interest
Amount =p*(1 + r/100)*t

CI=Amount-p
print(CI)
#percentage of 5 subject
s1,s2,s3,s4,s5=74,85,74,85,75
per=(s1+s2+s3+s4+s5)/5
print(per)
#celcius to frenhit
C=20
F = (C * 9/5) + 32
F=45
C = (F - 32) + 5/9
print(C)
#kilometer to meter
km=5
meter=km*1000
print(meter)
#hms
s=3756
h=s//3600
m=(s%3600)//10
rs=s%60
print(h , m , rs)
