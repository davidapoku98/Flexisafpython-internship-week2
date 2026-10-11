print("Your Receipt Calculator")
cost_of_item = float(input("Enter the cost of the item: "))
vat_rate = float(input("Enter the VAT rate (in %): "))
vat_amount = (cost_of_item * vat_rate) / 100
total_cost = cost_of_item + vat_amount
print(f"The amount you pay is: {total_cost}")