import streamlit as st
from supabase import create_client, Client

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="TFMatrix",
    page_icon="🔧",
    layout="wide",
)

# --------------------------------------------------
# Supabase connection
# --------------------------------------------------

@st.cache_resource
def get_supabase_client() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"],
    )


try:
    supabase = get_supabase_client()
    database_connected = True
except Exception as error:
    supabase = None
    database_connected = False
    connection_error = error


# --------------------------------------------------
# Database helpers
# --------------------------------------------------

def get_count(table_name: str) -> int:
    response = (
        supabase
        .table(table_name)
        .select("*", count="exact", head=True)
        .execute()
    )

    return response.count or 0


def get_rows(table_name: str, limit: int = 100):
    response = (
        supabase
        .table(table_name)
        .select("*")
        .limit(limit)
        .execute()
    )

    return response.data or []


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🔧 TFMatrix")
st.subheader("The Torque Factory Management System")

st.write(
    "A complete management platform for automotive repair shops."
)

st.divider()


# --------------------------------------------------
# Database status
# --------------------------------------------------

if database_connected:
    st.success("🟢 Connected to TFMatrix database")
else:
    st.error("🔴 Unable to connect to the TFMatrix database.")
    st.caption(str(connection_error))


# --------------------------------------------------
# Dashboard metrics
# --------------------------------------------------

if database_connected:

    try:
        customers_count = get_count("customers")
        vehicles_count = get_count("vehicles")
        work_orders_count = get_count("work_orders")
        invoices_count = get_count("invoices")

    except Exception as error:
        customers_count = 0
        vehicles_count = 0
        work_orders_count = 0
        invoices_count = 0

        st.warning(
            f"Database connection succeeded, but the dashboard "
            f"could not load the counts: {error}"
        )

else:
    customers_count = 0
    vehicles_count = 0
    work_orders_count = 0
    invoices_count = 0


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        customers_count,
    )

with col2:
    st.metric(
        "Vehicles",
        vehicles_count,
    )

with col3:
    st.metric(
        "Open Work Orders",
        work_orders_count,
    )

with col4:
    st.metric(
        "Invoices",
        invoices_count,
    )


st.divider()


# --------------------------------------------------
# TFMatrix navigation
# --------------------------------------------------

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


# --------------------------------------------------
# Dashboard
# --------------------------------------------------

if section == "Dashboard":

    st.subheader("Dashboard")

    if database_connected:
        st.success(
            "TFMatrix is connected to the Supabase database."
        )

        st.write(
            "Your database is ready for customer, vehicle, "
            "work order, invoice, and payment management."
        )

    else:
        st.info(
            "Connect the Supabase credentials to activate "
            "the TFMatrix database."
        )


# --------------------------------------------------
# Customers
# --------------------------------------------------

elif section == "Customers":

    st.subheader("Customers")

    if database_connected:

        try:
            rows = get_rows("customers")

            if rows:
                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.info("No customers have been added yet.")

        except Exception as error:
            st.error(f"Unable to load customers: {error}")

    else:
        st.warning("Database connection is not available.")


# --------------------------------------------------
# Vehicles
# --------------------------------------------------

elif section == "Vehicles":

    st.subheader("Vehicles")

    if database_connected:

        try:
            rows = get_rows("vehicles")

            if rows:
                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.info("No vehicles have been added yet.")

        except Exception as error:
            st.error(f"Unable to load vehicles: {error}")

    else:
        st.warning("Database connection is not available.")


# --------------------------------------------------
# Work Orders
# --------------------------------------------------

elif section == "Work Orders":

    st.subheader("Work Orders")

    if database_connected:

        try:
            rows = get_rows("work_orders")

            if rows:
                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.info("No work orders have been created yet.")

        except Exception as error:
            st.error(f"Unable to load work orders: {error}")

    else:
        st.warning("Database connection is not available.")


# --------------------------------------------------
# Estimates
# --------------------------------------------------

elif section == "Estimates":

    st.subheader("Estimates")

    st.info(
        "Estimate management will be built into TFMatrix next."
    )


# --------------------------------------------------
# Invoices
# --------------------------------------------------

elif section == "Invoices":

    st.subheader("Invoices")

    if database_connected:

        try:
            rows = get_rows("invoices")

            if rows:
                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.info("No invoices have been created yet.")

        except Exception as error:
            st.error(f"Unable to load invoices: {error}")

    else:
        st.warning("Database connection is not available.")


# --------------------------------------------------
# Payments
# --------------------------------------------------

elif section == "Payments":

    st.subheader("Payments")

    if database_connected:

        try:
            rows = get_rows("payments")

            if rows:
                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.info("No payments have been recorded yet.")

        except Exception as error:
            st.error(f"Unable to load payments: {error}")

    else:
        st.warning("Database connection is not available.")


# --------------------------------------------------
# Inventory
# --------------------------------------------------

elif section == "Inventory":

    st.subheader("Inventory")

    st.info(
        "Inventory management will be added in a future TFMatrix release."
    )


# --------------------------------------------------
# Technicians
# --------------------------------------------------

elif section == "Technicians":

    st.subheader("Technicians")

    st.info(
        "Technician management will be added in a future TFMatrix release."
    )


# --------------------------------------------------
# Shop Management
# --------------------------------------------------

elif section == "Shop Management":

    st.subheader("Shop Management")

    if database_connected:

        try:
            rows = get_rows("shops")

            if rows:
                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.info("No shops have been added yet.")

        except Exception as error:
            st.error(f"Unable to load shops: {error}")

    else:
        st.warning("Database connection is not available.")
