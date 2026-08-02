import logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

class DiscountCalculator:
    #constructor
    def __init__(self, price, discount_amount):
        self.price = price
        self.discount_amount = discount_amount
    
    def calculate_discount(self):
        """
        Calculate the discounted price based on the original price and discount amount.
        """
        try:
            
            final_price = self.price - float(self.discount_amount)
            logging.info(f"Calculation successful. Final price: {final_price}")
        except ValueError as e:
            logging.error(f"Error converting discount amount to float: {e}")
            return None
        return final_price

#==================================================================
calculator = DiscountCalculator(100, "abc")
result = calculator.calculate_discount()
