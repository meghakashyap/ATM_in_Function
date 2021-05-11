def language():
    if user==1:
        a= "English"
    else:
        a= "Hindi"
    return user
user=int(input("Choose your Langugae \n 1.English \n 2.Hindi \n...="))

def pin_code():
    if user==1:
        i=0
        while i<3:
            pin=int(input("enter your four digit pin number="))
            if pin== 1234:
                print("correct")
                break
            else:
                print("inncorect Pin!")
            i+=1
        else:
            print("............................")
            print("Your Credit Card is block")
          
    else:
        i=0
        while i<3:
            pin=int(input("Apna char number ka pin Darj kare="))
            if pin== 1234:
                print("Aapka pin sahi hai")
                break
            else:
                print("Fir se apna pin dale")
            i+=1
        else:
            print("............................")
            print("Your Credit Card is block")
    return pin     
code=pin_code()
def options():
    if user==1:
        if code==1234:
            balance=35000
            print('please press \n 1. for your balance inquiry')
            print('please press \n 2. for your withdrawl')
            print('please press \n 3. for your pay in')
            print('please press \n 4. for your return card/ Exit')
            print(".............")
            option=int(input('what would you like to choose='))
            if option ==1:
                print(balance,"Your current balance")
            elif option ==2:
                withdrwal=int(input("enter how much money would you like to withdrawl="))
                print(balance-withdrwal,"Your Current balance")
            elif option ==3:
                pay=int(input("enter how much money you want to pay in="))
                print( balance + pay,"you current balance")
            else:
                print("collect your card")
                print("THANK YOU FOR VISIT")
    
    else:
        if code==1234:
            balance=35000
            print('1.Kripya karke  1. dbaye apni Jma rashi ke bare me janne ke liye')
            print('2.Pese nikalne ke liye 2. Dbaye')
            print('3.Pese Jma karne ke liye 3. dbaye')
            print('4.Apna card wapis lene ke liye 4 dbaye')
            print("...........")
            option=int(input("kripya karke apna Vikalp chune="))
            if option ==1:
                print(balance,"Apki kul jma rashi")
            elif option ==2:
                withdrwal=int(input("Aap kitni rashi nikalna chahoge?="))
                print(balance-withdrwal,"apki kul jma rashi")
            elif option ==3:
                pay=int(input("Aap kitna Bhugtan karna chahoge?="))
                print(balance + pay,"Apki Kul Jma rashi")
            else:
                print("Apna card Jma kar lijiye")
                print("Dhanyawad Aane Ke liye")

def main():
    print(language())
    options()
main()
#Atm question in function


