import streamlit as st
import pandas as pd

data = [
    # Beverages
    {"Israeli Product": "Coca Cola", "Category": "Beverage", "Pakistani Alternative": "Pakola"},
    {"Israeli Product": "Pepsi", "Category": "Beverage", "Pakistani Alternative": "Mezan Cola"},
    {"Israeli Product": "7UP", "Category": "Beverage", "Pakistani Alternative": "FizUp"},
    {"Israeli Product": "Mountain Dew", "Category": "Beverage", "Pakistani Alternative": "Amrat Cola"},
    {"Israeli Product": "Sprite", "Category": "Beverage", "Pakistani Alternative": "Bubble Up"},
    {"Israeli Product": "Fanta", "Category": "Beverage", "Pakistani Alternative": "Amrat Orange"},
    # Food & Dairy
    {"Israeli Product": "Nestle", "Category": "Food & Dairy", "Pakistani Alternative": "Nurpur"},
    {"Israeli Product": "Maggi", "Category": "Food & Dairy", "Pakistani Alternative": "Kolson"},
    {"Israeli Product": "Oreo", "Category": "Food & Dairy", "Pakistani Alternative": "Bisconni Choco"},
    {"Israeli Product": "Kraft", "Category": "Food & Dairy", "Pakistani Alternative": "Millac Cheese"},
    {"Israeli Product": "Nido", "Category": "Food & Dairy", "Pakistani Alternative": "Everyday"},
    {"Israeli Product": "Cheetos", "Category": "Food & Dairy", "Pakistani Alternative": "Super Crisps"},
    {"Israeli Product": "Lays", "Category": "Food & Dairy", "Pakistani Alternative": "Snack City Chips"},
    {"Israeli Product": "Cerelac", "Category": "Food & Dairy", "Pakistani Alternative": "Lactogen"},
    # Fast Food Chains
    {"Israeli Product": "McDonald's", "Category": "Fast Food", "Pakistani Alternative": "OPTP"},
    {"Israeli Product": "KFC", "Category": "Fast Food", "Pakistani Alternative": "Al-Baik"},
    {"Israeli Product": "Burger King", "Category": "Fast Food", "Pakistani Alternative": "Burger Lab"},
    {"Israeli Product": "Pizza Hut", "Category": "Fast Food", "Pakistani Alternative": "Pizza Max"},
    {"Israeli Product": "Domino's", "Category": "Fast Food", "Pakistani Alternative": "Broadway Pizza"},
    # Cosmetics & Toiletries
    {"Israeli Product": "L'Oreal", "Category": "Cosmetics", "Pakistani Alternative": "Medora"},
    {"Israeli Product": "Garnier", "Category": "Cosmetics", "Pakistani Alternative": "WB by Hemani"},
    {"Israeli Product": "Maybelline", "Category": "Cosmetics", "Pakistani Alternative": "Rivaj UK"},
    {"Israeli Product": "Pantene", "Category": "Toiletries", "Pakistani Alternative": "Sunsilk Pakistan"},
    {"Israeli Product": "Head & Shoulders", "Category": "Toiletries", "Pakistani Alternative": "Clinic Plus"},
    {"Israeli Product": "Dove", "Category": "Toiletries", "Pakistani Alternative": "Medicam Soap"},
    {"Israeli Product": "Vaseline", "Category": "Toiletries", "Pakistani Alternative": "Hemani Petroleum Jelly"},
    # Tech & Electronics
    {"Israeli Product": "Intel", "Category": "Tech", "Pakistani Alternative": "AMD / Chinese Brands"},
    {"Israeli Product": "HP", "Category": "Tech", "Pakistani Alternative": "Lenovo / Huawei"},
    {"Israeli Product": "Motorola", "Category": "Tech", "Pakistani Alternative": "Infinix / Realme"},
    # Coffee & Café Chains
    {"Israeli Product": "Starbucks", "Category": "Coffee", "Pakistani Alternative": "Sattar Buksh"},
    {"Israeli Product": "Nescafe", "Category": "Coffee", "Pakistani Alternative": "Vital Café"},
    {"Israeli Product": "Costa", "Category": "Coffee", "Pakistani Alternative": "Chaye Khana"},
    {"Israeli Product": "Tim Hortons", "Category": "Coffee", "Pakistani Alternative": "Coffee Wagera"},
    # Clothing / Lifestyle Brands
    {"Israeli Product": "Puma", "Category": "Clothing", "Pakistani Alternative": "Service / Bata / Sputnik"},
    {"Israeli Product": "Nike", "Category": "Clothing", "Pakistani Alternative": "NDure"},
    {"Israeli Product": "Adidas", "Category": "Clothing", "Pakistani Alternative": "Servis Shoes"},
    {"Israeli Product": "Victoria’s Secret", "Category": "Clothing", "Pakistani Alternative": "Khaadi / Limelight"}
]

df = pd.DataFrame(data)

st.set_page_config(page_title="Boycott Israeli Products", page_icon="🛍️", layout="wide")
st.markdown("""
    <h1 style='text-align:center;color:#dc3545;'>🚫 Boycott Israeli Products – Support Local 🇵🇰</h1>
    <p style='text-align:center;'>This app helps you identify Israeli products and switch to Pakistani alternatives. Support your local economy!</p>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/00/Flag_of_Palestine.svg" width="300"/>
        <p>Free Palestine 🇵🇸</p>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Filter by Category")
    category_filter = st.selectbox("Select Category", ["All"] + sorted(df["Category"].unique()))

if category_filter != "All":
    filtered_df = df[df["Category"] == category_filter]
else:
    filtered_df = df


st.markdown("### 📋 Full Product List")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with 🤍 for Palestine.</p>", unsafe_allow_html=True)
