original_price = float(input("Enter price: "))
discount_percent = float(input("Enter discount %: "))

reduction = original_price * (discount_percent / 100)
discounted_price = original_price - reduction

   
print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {reduction:.2f}")
