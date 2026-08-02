import logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

def calculate_discount(price, discount_amount):
    """
    Calculate the discounted price based on the original price and discount amount.
    """
    try:
        
        final_price = price - int(discount_amount)
        logging.info(f"Calculation successful. Final price: {final_price}")
    except ValueError as e:
        logging.error(f"Error converting discount amount to integer: {e}")
        return None
    return final_price

#==================================================================
result = calculate_discount(100, "abc")
