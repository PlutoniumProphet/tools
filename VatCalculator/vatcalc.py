class Calculator(object):
    
    def __init__(self, receipt_value, vat_rate=1.20):
        self.receipt_value = receipt_value
        self.vat_rate = vat_rate

    def calc(self, receipt_value):
        """
        calculates net (pre-tax) value from receipt input
        and returns the tax amount applied (included in receipt value)
        to 2dp.
        """
        net_value = float(receipt_value) / self.vat_rate
        refund_vat = round(float(receipt_value) - net_value, 2)
            
        return refund_vat