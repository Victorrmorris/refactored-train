import streamlit as st
import plotly.graph_objects as go

# ---- Streamlit App Layout ----
st.title("🏦 International Bank & Payments Optimizer")
st.subheader("🔄 How Your Money Moves Across Accounts & Providers")

# ---- Define Banking & Payment Sources ----
accounts = [
    "U.S. Checking Account", "Wise (USD)", "PayPal (USD)", "Revolut (EUR)", 
    "German Checking Account", "Wise (EUR)", "PayPal (EUR)", "Credit Card (EUR)"
]

# Define Transactions (Source -> Target) & Associated Fees
source = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7]  # Where money starts
target = [1, 2, 3, 4, 5, 6, 5, 6, 7, 4, 5, 3]  # Where money flows
transaction_amounts = [2000, 500, 300, 800, 1200, 400, 1500, 900, 600, 1100, 700, 400]  # Amounts in USD
fees = [20, 5, 10, 15, 25, 8, 12, 18, 6, 10, 9, 5]  # Estimated transaction fees in USD

# Create Chord Diagram using Plotly Sankey (Closest Alternative)
fig = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=30,
        line=dict(color="black", width=0.5),
        label=accounts,
        color=["#007bff", "#00a86b", "#ff6f61", "#ffcc00", "#008000", "#28a745", "#ff4b5c", "#6a0dad"]
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
### **How to Read This Flow Diagram**
- **Left Side (Sources)**: Where money originates (e.g., U.S. Checking, Wise, PayPal).
- **Right Side (Destinations)**: Where money is sent (e.g., German Checking, Revolut, Credit Card).
- **Line Thickness**: Represents the **amount transferred** (wider = more money).
- **Color Coding**:
    - 🔵 **U.S. Accounts** (Checking, Wise, PayPal)
    - 🟢 **European Accounts** (German Bank, Revolut, Credit Card)
    - 🔴 **High-Fee Payment Providers** (PayPal)
- **Optimize Your Transactions**:
    - **Use Wise for lower fees** on large transfers.
    - **Avoid PayPal** for large USD-EUR conversions due to higher FX costs.
    - **Revolut offers fee-free spending in EUR** (good for daily purchases).
""")
