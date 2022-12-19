#https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload

print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollarcoaster!")
    age=int(input("What is your age? "))
    if age < 12:
        bill = 50
        print("Child ticket is 50 rupees")
    elif age <= 18:
        bill = 100
        print("Youth ticket is 100 rupees")
    else:
        bill = 200
        print("Adult ticket is 200 rupees")  
    want_photos=input("Do you want a photo taken? Y or N ")  
    if want_photos == "Y":
        bill +=20            #bill = bill + 20
        print(f"Please pay {bill}")  
    else:
        print(f"Please Pay {bill}")      
else:
    print("Sorry, you have to grow taller before you can ride")  