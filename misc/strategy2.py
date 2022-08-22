# Strategy class to handle the different strategies and return the output to the context
class Widget:
    def __init__(self, initial_price, discount_strategy = None):
        self.price = initial_price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount

    # The __repr__ function represents a class's object as a string.
    # If the print function is called on the class's object, it will return
    # the string defined in the __repr__ function.
    def __repr__(self):
        return f"Price: {self.price}, price after discount {self.price_after_discount()}"

# Concrete strategies that interface with the strategy
def ten_percent_discount(order):
    return order.price * 0.1

def fifteen_percent_discount(order):
    return order.price * 0.15

def twenty_percent_discount(order):
    return order.price * 0.2

# context which is responsible for interfacing with the strategy pattern
def main():
    print(Widget(100))
    print(Widget(100, discount_strategy=ten_percent_discount))
    print(Widget(100, discount_strategy=twenty_percent_discount))

if __name__ == "__main__":
    main()

