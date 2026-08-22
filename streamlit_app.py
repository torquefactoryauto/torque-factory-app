import streamlit as st

st.set_page_config(
    page_title="TFMatrix",
    page_icon="🔧",
    layout="wide",
)

# -----------------------------
# TFMatrix
# -----------------------------

st.title("🔧 TFMatrix")
st.subheader("The Torque Factory Management System")

st.write(
    "A complete management platform for automotive repair shops."
)

st.divider()

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Customers", "0")

with col2:
    st.metric("Vehicles", "0")

with col3:
    st.metric("Open Work Orders", "0")

with col4:
    st.metric("Outstanding Invoices", "$0.00")

st.divider()

# Navigation
st.header("TFMatrix")

section = st.selectbox(
    "Select a module",
    [
        "Dashboard",
        "Customers",
        "Vehicles",
        "Work Orders",
        "Estimates",
        "Invoices",
        "Payments",
        "Inventory",
        "Technicians",
        "Shop Management",
    ],
)

st.divider()

if section == "Dashboard":
    st.subheader("Dashboard")
    st.info("Your TFMatrix dashboard is ready. The next step is connecting it to your Supabase database.")

elif section == "Customers":
    st.subheader("Customers")
    st.info("Customer management will be connected to Supabase next.")

elif section == "Vehicles":
    st.subheader("Vehicles")
    st.info("Vehicle records will be connected to Supabase next.")

elif section == "Work Orders":
    st.subheader("Work Orders")
    st.info("Work order management will be connected to Supabase next.")

elif section == "Estimates":
    st.subheader("Estimates")
    st.info("Estimate creation will be added here.")

elif section == "Invoices":
    st.subheader("Invoices")
    st.info("Invoice management will be connected to Supabase next.")

elif section == "Payments":
    st.subheader("Payments")
    st.info("Payment tracking will be connected to Supabase next.")

elif section == "Inventory":
    st.subheader("Inventory")
    st.info("Parts and inventory management will be added here.")

elif section == "Technicians":
    st.subheader("Technicians")
    st.info("Technician management will be added here.")

elif section == "Shop Management":
    st.subheader("Shop Management")
    st.info("Multi-shop management will be connected to Supabase next.")
