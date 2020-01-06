VAT_RATE = 1.20

def calc():
    try:
        receipt_value = input("Enter receipt value: ")
        receipt_value = float(receipt_value)
        net_value = float(receipt_value) / VAT_RATE
        refund_vat = round(float(receipt_value) - net_value, 2)
        print(refund_vat)
        if input("Run again? ") == "y":
            calc()
        else:
            print("Bye!")
    except ValueError:
        print("You can only enter numbers!")
        calc()

calc()
