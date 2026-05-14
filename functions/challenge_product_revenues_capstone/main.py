# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
revenues = []
def calculate_revenue(prices, quantities):
    listing = zip(prices,quantities)
    local_revenues = []
    for price, quantity in listing:
        local_revenues.append(price*quantity) 
    return local_revenues
revenues=calculate_revenue(prices,quantities_sold)
revenue_per_product = list(zip(products,revenues))


def formatted_output(revenue_list):
    for product_name, revenue in sorted(revenue_list):
        print(f"{product_name} has total revenue of ${revenue}")
    return sorted(revenue_list)        

formatted_output(revenue_per_product)
# Example of expected output line (do not remove)
