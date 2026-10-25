import streamlit as st

st.title("🍔 Food Delivery Dashboard")

# 1. Customer Details
st.header("Customer Registration")
customer_name = st.text_input("Customer Name", "Priya")
phone = st.text_input("Phone Number", "9876543210")
address = st.text_input("Delivery Address", "Bangalore")

# 4. Wallet Top-up
st.header("Wallet")
wallet_amount = st.number_input("Add Money to Wallet", value=500)

# 3. Restaurant & Menu
st.header("Menu")
restaurant_name = st.selectbox("Choose Restaurant", ["Bawarchi (MG Road)"])
item_choice = st.multiselect("Select Items", ["Biryani (₹250)", "Kebab (₹180)"], default=["Biryani (₹250)", "Kebab (₹180)"])

# Order placement
if st.button("Place Order"):
    st.success(f"Order placed successfully for {customer_name} from {restaurant_name}!")
    st.info(f"Estimated Delivery Time: 30 mins")
    st.write(f"Delivery Partner Assigned: Rajesh (Bike)")
    st.balloons()
