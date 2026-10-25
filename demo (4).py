import sys
import time


class FoodDeliverySystem:

    def __init__(self):
        self.owner_name = "Nidhi Gadekar"
        self.menu = {
            1: {"name": "Truffle Crust Pizza", "price": 16.99, "category": "Italian"},
            2: {"name": "Wagyu Bacon Burger", "price": 14.50, "category": "American"},
            3: {"name": "Tuscan Chicken Pasta", "price": 15.00, "category": "Italian"},
            4: {"name": "Avocado Kale Salad", "price": 10.50, "category": "Healthy"},
            5: {"name": "Truffle Parmesan Fries", "price": 6.99, "category": "Sides"},
            6: {"name": "Belgian Chocolate Shake", "price": 6.50, "category": "Beverages"},
            7: {"name": "Artisan Cold Brew", "price": 4.50, "category": "Beverages"},
        }
        self.cart = {}
        self.promo_codes = {"WELCOME10": 0.10}  # 10% discount
        self.applied_discount = 0.0

    def display_header(self, title):
        print("\n" + "✨" * 22)
        print(f"       {title.upper()}       ")
        print("✨" * 22)

    def display_menu(self):
        self.display_header(f"{self.owner_name}'s Gourmet Menu")
        print(f"{'ID':<4} | {'Item Name':<26} | {'Category':<12} | {'Price':<6}")
        print("-" * 58)
        
        current_category = ""
        for item_id, details in self.menu.items():
            if details["category"] != current_category:
                current_category = details["category"]
                print(f"[{current_category.upper()}]")
            print(
                f"{item_id:<4} | {details['name']:<26} | {details['category']:<12} ${details['price']:<6.2f}"
            )
        print("-" * 58)

    def add_to_cart(self):
        self.display_menu()
        try:
            item_id = int(input("\n👉 Enter item ID to add: "))
            if item_id not in self.menu:
                print("❌ Invalid item ID. Please select from the menu above.")
                return

            quantity = int(input("👉 Enter quantity: "))
            if quantity <= 0:
                print("❌ Quantity must be at least 1.")
                return

            item = self.menu[item_id]
            if item_id in self.cart:
                self.cart[item_id]["quantity"] += quantity
            else:
                self.cart[item_id] = {
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": quantity,
                }

            print(f"Success! Added {quantity}x {item['name']} to your bag. 🛍️")

        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")

    def view_cart(self):
        if not self.cart:
            print("\n🛒 Your bag is currently empty.")
            return False

        self.display_header("Your Shopping Bag")
        print(f"{'Item Name':<25} | {'Qty':<4} | {'Price':<7} | {'Total':<7}")
        print("-" * 52)

        subtotal = 0.0
        for details in self.cart.values():
            item_total = details["price"] * details["quantity"]
            subtotal += item_total
            print(
                f"{details['name']:<25} | {details['quantity']:<4} | ${details['price']:<6.2f} | ${item_total:<6.2f}"
            )
        print("-" * 52)
        print(f"Subtotal: ${subtotal:.2f}")
        if self.applied_discount > 0:
            discount_amount = subtotal * self.applied_discount
            print(f"Promo Discount (-{int(self.applied_discount * 100)}%): -${discount_amount:.2f}")
        print("=" * 52)
        return True

    def apply_promo(self):
        code = input("\nEnter promo code (e.g., WELCOME10): ").strip().upper()
        if code in self.promo_codes:
            self.applied_discount = self.promo_codes[code]
            print(f"🎉 Success! Promo code '{code}' applied ({int(self.applied_discount * 100)}% off).")
        else:
            print("❌ Invalid or expired promo code.")

    def checkout(self):
        if not self.view_cart():
            return

        address = input("\n📍 Enter your delivery address: ").strip()
        if not address:
            print("❌ Address cannot be left blank.")
            return

        subtotal = sum(item["price"] * item["quantity"] for item in self.cart.values())
        discount_amount = subtotal * self.applied_discount
        discounted_subtotal = subtotal - discount_amount
        delivery_fee = 3.99
        tax = discounted_subtotal * 0.085  # 8.5% tax
        grand_total = discounted_subtotal + delivery_fee + tax

        self.display_header("Order Summary & Receipt")
        print(f"🏠 Delivery To : {address}")
        print(f"👤 Ordered By  : {self.owner_name}")
        print("-" * 45)
        print(f"Subtotal      : ${subtotal:.2f}")
        if self.applied_discount > 0:
            print(f"Discount      : -${discount_amount:.2f}")
        print(f"Delivery Fee  : ${delivery_fee:.2f}")
        print(f"Taxes (8.5%)  : ${tax:.2f}")
        print("-" * 45)
        print(f"GRAND TOTAL   : ${grand_total:.2f}")
        print("=" * 45)

        confirm = input("\nConfirm and place order? (y/n): ").strip().lower()
        if confirm == "y":
            print("\n🚀 Processing your order...")
            time.sleep(1)
            print("🍳 Chef is preparing your meal...")
            time.sleep(1)
            print("🚴 Rider assigned! Your food is on the way.")
            print(f"✨ Thank you for ordering from {self.owner_name}'s Kitchen!")
            self.cart.clear()
            self.applied_discount = 0.0
        else:
            print("❌ Checkout cancelled.")

    def run(self):
        while True:
            print("\n" + "═" * 42)
            print(f"    🍽️  {self.owner_name.upper()}'S KITCHEN  🍽️     ")
            print("═" * 42)
            print(" [1] Explore Menu")
            print(" [2] Add Item to Bag")
            print(" [3] View Bag & Apply Promo")
            print(" [4] Proceed to Checkout")
            print(" [5] Exit Application")
            print("═" * 42)

            choice = input("Select an option (1-5): ").strip()

            if choice == "1":
                self.display_menu()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.view_cart()
                if self.cart:
                    opt = input("\nWould you like to apply a promo code? (y/n): ").strip().lower()
                    if opt == "y":
                        self.apply_promo()
            elif choice == "4":
                self.checkout()
            elif choice == "5":
                print(f"\n👋 Thank you for visiting {self.owner_name}'s system. Goodbye!")
                sys.exit()
            else:
                print("❌ Invalid choice. Please pick a number from 1 to 5.")


if __name__ == "__main__":
    app = FoodDeliverySystem()
    app.run()
