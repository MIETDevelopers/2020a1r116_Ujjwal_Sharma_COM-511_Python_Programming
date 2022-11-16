a = input("What you want to Convert (C/F) : ")
if (a == "C") or (a == "c"):
    C = int(input("Enter the Temperature in Celsius : "))

    F = (C * (9/5)) + 32 

    print("Temperature in Farenheit is : %.2f °F" %(F))
    
elif (a == "F") or (a == "f"):
    F = int(input("Enter the Temperature in Farenheit : "))

    C = (F - 32) * (5/9) 

    print("Temperature in Celsius is : %.2f °C" %(C))
    
else:
    print("Please Enter the Valid Input...!!!")
