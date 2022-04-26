from weakref import ref


class banktransaction:

    date_operation  = ''
    date_payment    = ''
    description     = ''
    payment         = ''
    total           = ''
    reference       = ''

    def __init__(self, date_operation, date_payment, description, payment, total, reference):
        self.date_operation = date_operation
        self.date_payment = date_payment
        self.description = description
        self.payment = payment
        self.total = total
        self.reference = reference
    
    def printRecord(self):
        print("OperationDate  : " + self.date_operation)
        print("PaymentDate    :" + self.date_payment)
        print("Description    : " + self.description)
        print("Payment        :" + self.payment)
        print("Total          :" + self.total)
        print("Reference      :" + self.reference)