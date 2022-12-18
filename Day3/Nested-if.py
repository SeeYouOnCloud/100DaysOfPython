#https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1J7_rw1flGeF0hmc_zrMzPX7t6xkbcsiX%26export%3Ddownload
#https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload
# The only strict limit is that there can only be one if and one else per if/elif/else statement block, but there is no limit on the number of elif.
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollarcoaster!")
    age=int(input("What is your age? "))
    if age < 12:
        print("Please pay 50 rupees")
    elif age <= 18:
        print("Please pay 100 rupees")
    else:
        print("Please pay 200 rupees")    
else:
    print("Sorry, you have to grow taller before you can ride")    