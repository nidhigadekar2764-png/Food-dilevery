# 1. Register customer Priya with phone 9876543210 and address Bangalore.
# 2. Register delivery partner Rajesh with vehicle Bike.
# 3. Create Bawarchi at MG Road and add Biryani and Kebab.
# 4. Top up Priya's wallet by 500, then attempt a top-up of -100.
# 5. Priya places an order for Biryani and Kebab.
# 6. Print subtotal, GST, packaging fee, total, and estimated delivery time.
# 7. Rajesh accepts the order. Try a wrong OTP, then deliver using 1234.
# 8. Notify Priya and Rajesh using notify("Order delivered").

%%writefile demo.py
from food_delivery import Customer, DeliveryPartner, Restaurant, MenuItem

# 1. Register customer Priya with phone 9876543210 and address Bangalore.
priya = Customer("Priya", "9876543210", "Bangalore")

# 2. Register delivery partner Rajesh with vehicle Bike.
rajesh = DeliveryPartner("Rajesh", "9123456789", "Bike")

# 3. Create Bawarchi at MG Road and add Biryani and Kebab.
bawarchi = Restaurant("Bawarchi", "MG Road")
item1 = MenuItem("Biryani", 250, False)
item2 = MenuItem("Kebab", 180, False)
bawarchi.add_item(item1)
bawarchi.add_item(item2)

# 4. Top up Priya's wallet by 500, then attempt a top-up of -100.
priya.add_to_wallet(500)
priya.add_to_wallet(-100)

# 5. Priya places an order for Biryani and Kebab.
order = priya.place_order(bawarchi, [item1, item2])

# 6. Print subtotal, GST, packaging fee, total, and estimated delivery time.
subtotal = sum(item.price for item in order._items)
gst = subtotal * 0.05
packaging_fee = 20
total = order.calculate_bill()

print(f"Subtotal: {subtotal}")
print(f"GST (5%): {gst}")
print(f"Packaging Fee: {packaging_fee}")
print(f"Total Bill: {total}")
print(f"Estimated Time: {order.estimated_time()} mins")

# 7. Rajesh accepts the order. Try a wrong OTP, then deliver using 1234.
rajesh.accept_order(order)
rajesh.deliver(order, 9999)  # Invalid OTP test
rajesh.deliver(order, 1234)  # Valid OTP test

# 8. Notify Priya and Rajesh using notify("Order delivered").
priya.notify("Order delivered")
rajesh.notify("Order delivered")

%%writefile requirements.txt
streamlit
