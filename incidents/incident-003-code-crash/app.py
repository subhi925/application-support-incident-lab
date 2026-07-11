import logging
logging.basicConfig(filename="app.log", level=logging.INFO)

def calculate_discount(price, discount_amount):
    """
    Calculate the discounted price based on the original price and discount amount.
    """
    try:
        final_price = price - int(discount_amount)
    except ValueError as e:
        logging.error(f"Error converting discount amount to integer: {e}")
        return None
    return final_price

#==================================================================
result = calculate_discount(100, "abc")
