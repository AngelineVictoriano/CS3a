#/*****************************************************/
#/* CS03A - Summer 2026
#/* Lab 4
#/* Student Name: Angeline Victoriano
#/* SID: 20528831
## /***************************************************/

#TOTAL SALES

def total_sales(sales_list):
    total_sale_in_usd = 0
    for sale in sales_list:
        total_sale_in_usd += sale
    return total_sale_in_usd

def main():
    sales_list = []
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday"]

    try:
        for day in days_of_the_week:
            day_sale = float(input(f"Enter the store's sale for {day}: $"))
            sales_list.append(day_sale)
        print(f"The week's total sales is ${total_sales(sales_list):.2f}")
    except ValueError:
        print("Enter only numbers. Starting over...")
        main()



main()

#DATE PRINTER

print("\n\n\n\n")
date_entered = input('Enter the date in the format "mm/dd/yyyy": ')

months = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December"
          ]
def date_converter(date_entered):
    month = int(date_entered[0:2])
    if date_entered[3] == "0":
        day = date_entered[4]
    else:
        day = date_entered[3:5]
    year = date_entered[6:10]

    print(f"The date entered is: {months[month-1]} {day}, {year}")
date_converter(date_entered)