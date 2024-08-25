"""
#
# Part: Python While Loop
#
"""

i = 1
while i < 5:
    print("i = ", i)
    i+=1    # i = i + 1

i = 1
while i < 5:
    print("i = ", i)
    if i == 3:
        break
    i+=1   

"""
i = 1
while i < 5:
    print("i = ", i)
    if i == 3:
        continue
    i+=1
"""

i = 1
while i < 5:
    print("i = ", i)
    i+=1
else:
    print("Game Over!")

"""
#
# Part: Python For Loop
#
"""

fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    print("Fruit:", fruit)

for fruit in fruits:
    print("Fruit:", fruit)
    if fruit == "banana":
        break                   

for fruit in fruits:
    if fruit == "banana":
        break                   #ถ้าเจอ banana ให้หยุดการทำงานลูป
    print("Fruits: ",fruit)

for fruit in fruits:
    if fruit == "banana":
        continue                #ถ้าเจอ banana ให้ข้ามลูป
    print("Fruits: ",fruit)

for x in range(len(fruits)):    #วนลูปตามจำนวนตัวแปร
    print("Number:", x)

for x in range(5):              #วนลูปตามจำนวน
    print("Number:", x)
else:
    print("Game Over!")

adjs = ["red", "blue", "green"] #ลูปในลูป ให้ซ้ำได้มากสุด 4 ชั้น 
fruits = ["apple", "banana", "coconut"]
for adj in adjs:
    for fruit in fruits:
        print("Fruits : " + adj + " " + fruit)