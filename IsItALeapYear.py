#Leap year is every year that is evenly divisible by 4   
#**except** every year that is evenly divisible by 100   
#**unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))
year4=year%4
year100=year%100
year400=year%400

if year4==0: 
    if year100==0:
        if year400==0:
            print("Leap year.")
        else:
             print("Not leap year.")
    else:
        print("Leap year.")

else:
    print("Not leap year.")
        
