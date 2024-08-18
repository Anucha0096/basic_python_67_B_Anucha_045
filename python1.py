"""
#
# Part: Python Comment 
#
"""

# this a comment
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m) 
# t = เวลา (s)

"""
this a comment
v = s/t
v = ความเร็ว (m/s)
s = ระยะทาง (m) 
t = เวลา (s)
"""
print("Hello World!!!")

#-----------------------------------------------

"""
#
# Part: Python Variables 
#
"""

#-------------------------------------------

x = 5               #Integer
y = "Hey Bruh"      #String
print (x,y )

x = str(3) 
y = int(5)
z = float(7)
print(type(x), type(y), type(z))

"""
#
# Part: Python Variables Names
#
"""

myvar = "John"
my_var = "John"
_my_var = "John"    #นิยม
myVar = "John"      #นิยม
MYVAR = "John"      #สำหรับข้อมูลคงที่
MY_VAR = "John"     #นิยม
my_var2 = "John"
#2my_var = "John"   #ห้ามใช้
#my-var = "John"    #ห้ามใช้
#my var = "John"    #ห้ามใช้

# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"

"""
#
# Part: Python String
#
"""

x = "Hey Bruh"
print(x)

y = """1 Hey Bruh
2 Hey Bruh
3 Hey Bruh
"""
print(y)

#ให้แสดงผล x อักษร ค่าที่ 2 รวม 0
x = "Hey Bruh"
print(x[2])
print(len(x))       #หาค่าความกว้างของข้อมูล

print("Hey" in x)   #ให้หาคำว่า Hey ในตัวแปร x 
print("What sup" not in x) 
print(x.upper())    #ให้ค่าเป็นตัวใหญ่ทั้งหมด
print(x.lower())    #ให้ค่าเป็นตัวเล็ก

print(x.replace("Bruh", "Sis")) #โค้ดการแทนคำ
print(x.split("  "))            #ตัดคำ
a = "Apple"
b = "Company"
print( a + " " + b )            #โค้ดรวมคำ


price = 20
word = f"Price: {price:.2f}"    #แสดงค่า Price เป็นทศนิยม 2 ตำแหน่ง
print(word)