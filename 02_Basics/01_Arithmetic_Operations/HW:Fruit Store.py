#!/usr/bin/python3

# Items
apple_price_per_piece = 12
apple_qty_dozens = 5  # in dozens
mango_price_per_piece = 34
mango_qty_dozens = 3  # in dozens

# Quantity
apple_qty_pieces = apple_qty_dozens * 12  # 1 dozen = 12 pieces
mango_qty_pieces = mango_qty_dozens * 12  # 1 dozen = 12 pieces

# Amount
apple_amount = apple_price_per_piece * apple_qty_pieces
mango_amount = mango_price_per_piece * mango_qty_pieces

# Total Amount
total_amount = apple_amount + mango_amount
print("Total Amount  : ", total_amount)

# Discount
discount_percent = 2
discount_amount = (discount_percent / 100) * total_amount
amount_after_discount = total_amount - discount_amount
print("Discount Amount: ", round(discount_amount, 2))

# GST
gst_percent = 12.5
gst_amount = (gst_percent / 100) * amount_after_discount
final_amount = amount_after_discount + gst_amount
print("GST Amount    : ", round(gst_amount, 2))

# To Display the final billable amount
print("Final Billable Amount: ", round(final_amount, 2))

########################
# constants
DOZEN = 12
DISCOUNT = 2
GST = 12.5

# cost of fruits
cost_of_apple = 12  # per piece
cost_of_mango = 34  # per piece

# Quantities of fruits
qty_of_apples = 5 * DOZEN  # pieces
qty_of_mangos = 3 * DOZEN  # pieces

# Selling Price Computation
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos  # PEDMAS
# total_sp =(cost_of_apple * qty_of_apples) + (cost_of_mango * qty_of_mangos)  # PEDMAS
print("Total Selling Price :", total_sp)

# Discount Calculation
discount_amount = (total_sp * DISCOUNT) / 100
print("Discount Amount     :", discount_amount)

# Payable Amount Calculation
payable_amount = total_sp - discount_amount
print("Payable Amount      :", payable_amount)

# GST Calculation
gst_on_fruits = (payable_amount * GST) / 100
print("GST on Fruits       :", gst_on_fruits)

# Billable Amount Calculation
billable_amount = payable_amount + gst_on_fruits
print("Billable Amount     :", billable_amount)

# round(num, no_of_digits) - function
print("Billable Amount(r)  :", round(billable_amount, 2))