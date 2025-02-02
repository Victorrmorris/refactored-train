import streamlit as st
import plotly.graph_objects as go

# ---- Streamlit App Layout ----
st.title("🏦 International Bank & Payments Optimizer")
st.subheader("💸 How Your Money Moves Across Accounts & Providers")

# ---- Define Banking & Payment Sources ----
accounts = [
    "US Bank", "Wise (USD)", "PayPal (USD)", "Revolut (EUR)", 
    "German Bank", "Wise (EUR)", "PayPal (EUR)", "Credit Card"
]

# Define Transactions (Source -> Target) & Associated Fees
source = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7]  # US Bank, Wise, PayPal, Revolut, etc.
target = [1, 2, 3, 4, 5, 6, 5, 6, 7, 4, 5, 3]  # Flowing into Wise, PayPal, German Bank, etc.
transaction_amounts = [2000, 500, 300, 800, 1200, 400, 1500, 900, 600, 1100, 700, 400]  # Amounts in USD
fees = [20, 5, 10, 15, 25, 8, 12, 18, 6, 10, 9, 5]  # Estimated transaction fees in USD

# Create Chord Diagram using Plotly Sankey (Closest Alternative)
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=accounts,
        color=["blue", "green", "orange", "purple", "red", "cyan", "pink", "gray"]
    ),
    link=dict(
        source=source,
        target=target,
        value=transaction_amounts,
        color=["rgba(31, 119, 180, 0.6)" for _ in transaction_amounts]  # Transparent blue for flows
    )
))

# Display the Chart
st.plotly_chart(fig, use_container_width=True)

# ---- Explanation Section ----
st.markdown("""
### **How to Read This Chord Diagram**
- **Left Side**: Where money originates (e.g., US Bank, Wise, PayPal).
- **Right Side**: Where money ends up (e.g., German Bank, Revolut, Credit Card).
- **Line Thickness**: Represents the **amount transferred**.
- **Color Intensity**: Shows transaction **flow strength**.
- **Optimize by Choosing Lower-Fee Paths** (e.g., Wise vs. PayPal for USD to EUR conversion).
""")
