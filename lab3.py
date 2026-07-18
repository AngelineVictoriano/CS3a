# /*****************************************************/
# /* CS03A - Summer 2026
# /* Lab 2
# /* Student Name: Angeline Victoriano
# /* SID: 20528831
## /***************************************************/

def ticket_sales_income(atix, btix, ctix):
    income = 20*atix+ 15*btix + 10*ctix
    return income

def main():
    try:
        aSold = int(input("How many class A tickets were sold? "))
        bSold = int(input("How many class B tickets were sold? "))
        cSold = int(input("How many class C tickets were sold? "))
        total = ticket_sales_income(aSold, bSold, cSold)

        print(f"The total sales generated is ${total}")
    except ValueError:
        print("Enter only integers!")
        main()


main()