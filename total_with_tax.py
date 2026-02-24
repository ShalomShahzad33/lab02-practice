def total_with_tax(price, tax_rate):
    tax = price * tax_rate
    total = price + tax

    return total


print(total_with_tax(100, 0.15))
