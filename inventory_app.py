import streamlit as st
import pandas as pd

st.set_page_config(page_title="📦 Inventory Stock Tracker", layout="wide")
st.title("📦 Inventory Stock Tracking System – Filtered View")

uploaded_file = st.file_uploader("📤 Upload Cleaned Inventory CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        # 🚫 Remove Grand Total row if present
        df = df[df["Product Name"].str.lower().str.strip() != "grand total"]

        # === Basic Sidebar Filters ===
        st.sidebar.header("🔎 Filter Options")
        search_term = st.sidebar.text_input("🔍 Search Product Name")

        move_filter = st.sidebar.multiselect(
            "📦 Movement Status",
            options=["Moved", "Not Moved"],
            default=["Moved", "Not Moved"]
        )

        # === Apply Filters ===
        filtered_df = df[df["Movement Status"].isin(move_filter)]

        if search_term:
            filtered_df = filtered_df[filtered_df["Product Name"].str.contains(search_term, case=False)]

        # === Filtered Grand Totals ===
        st.markdown("### 📊 Grand Totals (Filtered)")
        total_opening = filtered_df["Opening Value"].sum()
        total_inward = filtered_df["Inward Value"].sum()
        total_outward = filtered_df["Outward Value"].sum()
        total_closing = filtered_df["Closing Value"].sum()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("🏁 Opening Value", f"₹ {total_opening:,.2f}")
            st.metric("📥 Inward Value", f"₹ {total_inward:,.2f}")
        with col2:
            st.metric("📤 Outward Value", f"₹ {total_outward:,.2f}")
            st.metric("📦 Closing Value", f"₹ {total_closing:,.2f}")

        # === Filtered Table ===
        st.markdown("### 📋 Inventory Details (Filtered View)")
        st.dataframe(filtered_df, use_container_width=True)

        # === 🎯 Filter by Specific Products ===
        st.sidebar.markdown("---")
        st.sidebar.subheader("🎯 Filter by Specific Products")

        product_options = df["Product Name"].unique().tolist()
        selected_products = st.sidebar.multiselect("Select Product(s)", product_options)

        if selected_products:
            selected_df = df[df["Product Name"].isin(selected_products)]

            st.markdown("### 🎯 Selected Product Summary")
            colA, colB = st.columns(2)
            with colA:
                st.metric("🏁 Opening Value", f"₹ {selected_df['Opening Value'].sum():,.2f}")
                st.metric("📥 Inward Value", f"₹ {selected_df['Inward Value'].sum():,.2f}")
            with colB:
                st.metric("📤 Outward Value", f"₹ {selected_df['Outward Value'].sum():,.2f}")
                st.metric("📦 Closing Value", f"₹ {selected_df['Closing Value'].sum():,.2f}")

            st.markdown("### 🧾 Selected Product Details")
            st.dataframe(selected_df, use_container_width=True)

        # === Download filtered CSV ===
        csv_download = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Filtered CSV", data=csv_download, file_name="filtered_inventory.csv", mime="text/csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("📤 Please upload the `cleaned_inventory_complete.csv` file to begin.")
