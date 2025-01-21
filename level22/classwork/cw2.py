#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, 
# გამოიყენეთ for loop

user_number = int(input("enter you number"))
sum = 0
for i in range(user_number):
    sum = sum + 2

print(sum)