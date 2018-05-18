from VatCalc import Calculator

# initialise instance and run calc
def calc_vat(receipt_value):
    myReceipt = Calculator(receipt_value)
    return myReceipt.calc(receipt_value)

# captures user input of receipt and converts to float. Handles input error
def get_vat():
    try:
        receipt_in = input("Enter receipt value: ")
        receipt_value = float(receipt_in)
        return calc_vat(receipt_value)
    except ValueError:
        return "You can only enter numbers!"

# trigger for loop 
def keep_going():
    return input("Run again? ") == "y"

# first pass
print(get_vat())    
while keep_going():
    print(get_vat())