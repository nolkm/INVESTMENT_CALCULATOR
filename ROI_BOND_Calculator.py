#ROI ON BOND CALCULATOR

def main():
    print("/Welcome to the ROI Estimator\ ")#print Statment welcoming to program


    bondInput()#calling bondFunction 
    #end of main()


def bondInput():
    valid = False#creating a looping varible 
    while valid == False:
            try:
                principal = float(input("Please enter the amount you would like to invest: "))#principal
                yeild = float(input("Please enter the Yeild rate(Intrest one the investment: "))#intrest
                mer = float(input("please enter the mer rate: "))#mer rate 
                period = int(input("Please enter the period of the bond: "))#length/period
                valid = True
            except ValueError:
                print("Please enter a valid numeric Value ")

            #calculation
            value = (principal * (yeild/100)) - ((principal * (mer/100)) - principal)
            print(f"ROI on the bond is {value} ")
        #end of bondInput()

main()
