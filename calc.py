def calculate_discount(price, discount_percent):
    """
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.
    
    Returns:
        float: The price after the discount has been applied.
    """
    if discount_percent >=20:
        discount amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    if __name__ == "__main__":
        # Enter the original price of the item
        price = float(input("Enter the original price of the item: kshs"))

        # Enter the discount percentage
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price after applying discount
        final_price = calculate_discount(price, discount_percent)

        # print the final price after applying the discount
        print(f"The price after a {discount_percent}% discount is: kshs{final_price:.2f}")