'''
Write a program that asks the user to enter the number of packages purchased.
 The program should then display the amount of the discount(if any) and the total
 amount of the purchase after the discount.
'''

quantity  = int(input(f"Please enter number of packages purchased:  "))

retail_price = 99.00
total_retail_price =  quantity * retail_price


if quantity >=10 and quantity <= 19:
    discount = retail_price * .10 * quantity
    total_discount = total_retail_price - discount

    print(f"Your discount is 10% savings of  {discount} totalPrice : {total_retail_price} purchase after the discount:{total_discount}")
elif quantity >=20 and quantity <=49:
    discount = retail_price * .20 * quantity
    total_discount = total_retail_price - discount
    print(f"Your discount is 20% savings of  {discount} totalPrice : {total_retail_price} purchase after the discount:{total_discount}")
elif quantity >= 50 and quantity <= 99:
    discount = retail_price * .30 * quantity
    total_discount = total_retail_price - discount
    print(f"Your discount is 30% savings of {discount} totalPrice : {total_retail_price} purchase after the discount:{total_discount}")
elif quantity >= 100:
    discount = retail_price * .40 * quantity
    total_discount = total_retail_price - discount
    print(f"Your discount is 40% savings of {discount} totalPrice : {total_retail_price} purchase after the discount:{total_discount}")
elif quantity <=10:
    print(f" Your discount is 0% savings of {quantity} totalPrice : {total_retail_price} purchase therefore no discount:")
