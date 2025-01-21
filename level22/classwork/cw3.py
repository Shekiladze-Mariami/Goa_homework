#3) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ერთიდან ამ რიცხვამდე მხოლოდ ლუწი რიცხვების ჯამი 
# ცალკე და მხოლოდ კენტი რიცვხების ჯამი ცალკე, გამოიყენეთ for loop

user_number = int(input("enter number:   "))

sum1 = 1
sum2 = 1
for i in range(user_number):
    sum1 = sum1 + 2
    sum2 = sum2 + 3

print(sum2)
print(sum1)