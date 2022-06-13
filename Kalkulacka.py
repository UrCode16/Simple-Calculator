import time
import keyboard

#Made by Ur Manager (@UrCode16 on GitHub)
#Thanks for using this code!
#Enjoy your simple keyboard

ver = 2.5 #Version

print(f"Welcome to my calculator version: {ver}")
print("GitHub: @UrCode16")
A = input("\nChoose operation (+, -, *, /): ")
B = int(input("Choose the first number: "))
C = int(input("Choose the second number: "))

if A == "+":
    print("The answer is:", B+C)

if A == "-":
    print("The answer is:", B-C)

if A == "*":
    print("The answer is:", B*C)

if A == "/":
    print("The answer is:", B/C)

time.sleep(1)

print("\nIf u want calculate something else press Enter", end="")

run = True
while run == True:
    if keyboard.is_pressed("Enter"):
        input("")
        A = input("Choose operation (+, -, *, /): ")
        B = int(input("Choose the first number: "))
        C = int(input("Choose the second number: "))
            
        if A == "+":
            print("The answer is:", B+C)
            
        if A == "-":
            print("The answer is:", B-C)
            
        if A == "*":
            print("The answer is:", B*C)
            
        if A == "/":
            print("The answer is:", B/C)
            
        time.sleep(1)
            
        print("\nIf u want calculate something else press Enter")
        time.sleep(0.5)
        print("If not press Esc")
    if keyboard.is_pressed("Esc"):
        run = False
print("Bye!")
time.sleep(1)