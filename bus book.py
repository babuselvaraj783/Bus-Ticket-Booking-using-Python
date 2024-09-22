
print("WELCOME TO BLUE BUS!!!")
print("OUR BUS ROUTE DETAILS:")
print("1) Chennai to Coimbatore")
print("2) Chennai to Salem")
print("3) Chennai to Kallakurchi")
print("4) Chennai to Tiruchirappalli")
print("5) Chennai to Tiruppur")
print("6) Chennai to Madurai")
print("7) Chennai to Perambalur")
print("8) Chennai to Ramanathapuram")
print("9) Chennai to Pudukottai")
print("10) Chennai to Thoothukudi")
# select your route 
for i in range (1,11):
    route = int(input("Select the bus route for your journey:"))
    if(route ==1):
        print ("you select Chennai to Coimbatore ")
        break
    elif(route ==2):
        print ("you select Chennai to Salem ")
        break
    elif(route ==3):
        print ("you select Chennai to Kallakurchi ")
        break
    elif(route ==4):
        print ("you select Chennai to Tiruchirappalli ")
        break
    elif(route ==5):
        print ("you select Chennai to Tiruppur  ")
        break
    elif(route ==6):
         print ("you select Chennai to Madurai ")
         break
    elif(route ==7):
        print ("you select Chennai to Perambalur  ")
        break
    elif(route ==8):
        print ("you select Chennai to Ramanathapuram  ")
        break
    elif(route ==9):
        print ("you select Chennai to Pudukottai ")
        break
    elif(route ==10):
        print ("you select Chennai to Thoothukudi ")
        break
    else:
        print("invalid bus route ")
       

print("Your bus route selected successfully!!!")
print("Select the timing")
print("1) 6.00 to 9.00")
print("2) 9.00 to 12.00")
print("3) 12.00 to 15.00")
print("4) 15.00 to 20.00")
#select timing
for j in range (1,4):
    time = int(input("Enter the timing:"))
    if (time == 1):
        print("you selected 6.00 to 9.00")
        break
    elif (time == 2):
        print("you selected 9.00 to 12.00")
        break
    elif (time == 3):
        print("you selected 12.00 to 15.00")
        break
    elif (time == 4):
        print("you selected 15.00 to 20.00")
        break
    else:
        print("invalid time")
print("Time selected sucessfully!!!")
print("Seat preferance:")
print("1)Ac Seater")
print("2)Ac Slepper")
print("3)NON Ac Seater")
print("4) NON Ac Slepper")
#select seat
for k in range(1,5):
    seat = int(input("Enter Seat Preferance:"))
    if(seat==1):
        print("you selected Ac seater")
        break
    elif(seat==2):
        print("you selected Ac slepper")
        break
    elif(seat==3):
        print("you selected non ac seater")
        break
    elif(seat==4):
        print("you selected non ac slepper")
        break
    else:
        print("invalid selection")
print("Seat selected successfully!!!")
print("Select your bus:")
print("1) SKT")
print("2) KPN")
print("3) BABU")
print("4) VETRI")
print("5) SBS")
#select bus
for a in range (1,6):
    bus = int(input("ENTER YOUR BUS NAME:"))
    if (bus==1):
        print("you selected skt bus")
        break
    elif(bus==2):
        print("you selected kpn bus")
        break
    elif(bus==3):
        print("you selected babu bus")
        break
    elif(bus==4):
        print("you selected vetri bus")
        break
    elif(bus==5):
        print("you selected sbs bus")
        break
    else:
        print("invalid bus")
print("Bus selected successfully!!!")
print("select breath preference:")
print("1to30")
#select seat no
for l in range (1,31):
    o = int(input("enter seat num:"))
    if (o <31):
        print("your seat is booked successfully")
        break
    else:
        print("invalid num")


print(" select your boarding point:")
print("1) Koyembedu bus stand")
print("2) Kilambakkam bus stand")
#select boarding point
for b in range(1,3):
    boarding = int(input("Enter boarding point:"))
    if(boarding==1):
        print("you selected Koyembedu bus stand")
        break
    elif(boarding==2):
        print("you selected Kilambakkam bus stand")
        break
    else:
        print("invalid boarding point")
        
print("Boarding point selected successfully!!!")
print("Select dropping point")
#select droping point
if (route == 1):
    print("1) Gandhipuram")
    print("2) Ukkadam")
elif (route == 2):
    print("1) Salem New Bus Stand")
    print("2) Salem Old Bus Stand")
elif (route == 3):
    print("1) Kallakurichi New Bus Stand")
    print("2) Kallakurichi Old Bus Stand")
elif (route == 4):
    print("1) Central Bus Stand")
    print("2) Srirangam Bus Stand")
elif (route == 5):
    print("1) Tiruppur New Bus Stand")
    print("2) Tiruppur Old Bus Stand")
elif (route == 6):
    print("1) Mattuthavani Bus Stand")
    print("2) Periyar Bus Stand")
elif (route == 7):
    print("1) Perambalur New Bus Stand")
    print("2) Perambalur Old Bus Stand")
elif (route == 8):
    print("1) Ramanathapuram New Bus Stand")
    print("2) Ramanathapuram Old Bus Stand")
elif (route == 9):
    print("1) Pudukottai New Bus Stand")
    print("2) Pudukottai Old Bus Stand")
elif (route == 10):
    print("1) Thoothukudi New Bus Stand")
    print("2) Thoothukudi Old Bus Stand")
else:
    print("invalid dropping point")

for d in range(1, 3):
    drop_point = int(input("Enter dropping point: "))
    if drop_point in [1, 2]:
        print("You dropping point selected successfully!!!")
        break
    else:
        print("Invalid dropping point")

print("Enter your Deatils")
#enter your deatils
Name = input("Name:")
Age = int(input("Age:"))
phone_no = int(input("Phone Number:"))
mailid = input("Email.id:")
while True:
    import random
    k=random.randint(0000,9999)
    print("otp is:",k)
    l=int(input("enter otp:"))
    if (k==l):
        print("otp is correct")
        break
    else:
        print("incoorect otp")
        
print ("Your deatils upload successfully!!!")
print ("HAPPY JOURNEY!!!")







    




