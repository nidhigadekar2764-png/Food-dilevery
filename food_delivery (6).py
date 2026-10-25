import streamlit as st

st.title("Food Delivery App")
st.write("Welcome to your food delivery dashboard!")

# Add a simple interactive widget
menu_item = st.selectbox("Choose your food:", ["Pizza", "Burger", "Pasta"])
if st.button("Order Now"):
    st.success(f"You successfully ordered {menu_item}!")
