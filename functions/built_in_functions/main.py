# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []


for product, values in products.items():
    price, quantity = values
    
    float_price = float(price)
    int_quantity = int(quantity)
    total_item_sales = float_price*int_quantity
    total_sales_list.append(total_item_sales)
    print(f"Total sales for {product}: ${total_item_sales}")
    total_sum = sum(total_sales_list)
    min_sales = min(total_sales_list)
    max_sales = max(total_sales_list)

print(f"Total sum of all sales: $",total_sum)
print(f"Minimum sales: ${min_sales}")
print("Maximum sales: $",max_sales)
      








