def main():
    M=int(input("Enter your Number Month : "))
    A=int(input("Entey the amount of your loan : "))
    r=float(input("Enter your monthly interest rate in percentage form : "))
    R=r/100

    P=(R*A)/1-(1-R)**M

    print(f"The monthly payment amount based in the {M} month is : {format(P,',.4f')} Dollar ")

main()
