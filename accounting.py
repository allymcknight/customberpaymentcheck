def customerpaymentcheck(log_file):
    melon_price = 1
    for order in log_file:
        data = order.split("|")
        customer_name = data[1]
        melons_bought = int(data[2])
        amount_paid = float(data[3])
        if amount_paid != melons_bought * melon_price:
            print customer_name + ", did not pay correctly"
            pay_difference = (melons_bought * melon_price) - amount_paid
            print customer_name + " still owes %s."% (pay_difference)


customerpaymentcheck(open("customer-orders.txt"))