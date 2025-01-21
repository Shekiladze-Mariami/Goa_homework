#4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ 5 ის ჯერადი რიცხვების 
# ჯამი ცალკე და მხოლოდ 3ის ჯერადი რიცხვების ჯამი ცალკე, გამოიყენეთ while loop

number = int(input("enter number:  "))
sum = 0
i = 0
sum1 = 0
i1 = 0

while i < 50:
    sum = sum + i
    i = i + 5
    sum1 = sum1 + i1
    i1 = i1 + 3
print(sum)
print(sum1)

