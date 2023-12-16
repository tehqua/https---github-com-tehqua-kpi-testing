import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.title("KPI count for Envestor club - only for this project")

    kpi_for_sale = st.number_input("Enter KPI for team sale", min_value=0.0, max_value=1.0, step=0.01)
    kpi_for_others = st.number_input("Enter KPI for others", min_value=0.0, max_value=1.0, step=0.01)
    target = 327000000
    products = {
        "product1": {"name": "Trà Lan Kim Tuyến - Hoàng Trà", "price": 250000},
        "product2": {"name": "Rượu Lan Kim Tuyến - Rượu Lan Gấm", "price": 2000000},
        "product3": {"name": "Mật ong ngâm - Mật Lan", "price": 450000}
    }
    sales = 30
    others = 15
    st.subheader("**Product Details**")
    st.write(f"- Product 1: {products['product1']['name']} (Price: {products['product1']['price']} VND)")
    st.write(f"- Product 2: {products['product2']['name']} (Price: {products['product2']['price']} VND)")
    st.write(f"- Product 3: {products['product3']['name']} (Price: {products['product3']['price']} VND)")

    if kpi_for_sale > 0 and kpi_for_sale < 1:
        kpi_per_day = (target * kpi_for_sale) / (30 * 4 * 30)
        kpi_per_week = (target * kpi_for_sale) * 7 / (30 * 4 * 30)
        product1_per_week = kpi_per_week / products["product1"]["price"]
        product2_per_week = kpi_per_week / products["product2"]["price"]
        product3_per_week = kpi_per_week / products["product3"]["price"]
        kpi_per_month = (target * kpi_for_sale) / (30 * 4)
        product1_per_month = kpi_per_month / products["product1"]["price"]
        product2_per_month = kpi_per_month / products["product2"]["price"]
        product3_per_month = kpi_per_month / products["product3"]["price"]
        kpi_all_project = (target * kpi_for_sale) / 30
        product1_all = kpi_all_project / products["product1"]["price"]
        product2_all = kpi_all_project / products["product2"]["price"]
        product3_all = kpi_all_project / products["product3"]["price"]
    else:
        st.error("KPI for team sale must be > 0 and < 1")

    if kpi_for_others > 0 and kpi_for_others < 1:
        kpi_per_day_o = (target * kpi_for_others) / (30 * 4 * 30)
        kpi_per_week_o = (target * kpi_for_others) * 7 / (30 * 4 * 30)
        product1_per_week_o = kpi_per_week_o / products["product1"]["price"]
        product2_per_week_o = kpi_per_week_o / products["product2"]["price"]
        product3_per_week_o = kpi_per_week_o / products["product3"]["price"]
        kpi_per_month_o = (target * kpi_for_others) / (30 * 4)
        product1_per_month_o = kpi_per_month_o / products["product1"]["price"]
        product2_per_month_o = kpi_per_month_o / products["product2"]["price"]
        product3_per_month_o = kpi_per_month_o / products["product3"]["price"]
        kpi_all_project_o = (target * kpi_for_others) / 30
        product1_all_o = kpi_all_project_o / products["product1"]["price"]
        product2_all_o = kpi_all_project_o / products["product2"]["price"]
        product3_all_o = kpi_all_project_o / products["product3"]["price"]
    else:
        st.error("KPI for others must be > 0 and < 1")

    if kpi_for_sale > 0 and kpi_for_others > 0:
        st.balloons() 
        st.subheader("Sales")
        st.write("KPI for Team Sale:")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"- KPI per day: {kpi_per_day:.2f} VND")
            st.write(f"- KPI per week: {kpi_per_week:.2f} VND")
            st.write(f"- KPI per month: {kpi_per_month:.2f} VND")

        with col2: 
            st.subheader("**Week**")
            st.write(f"- Product 1 per week: {product1_per_week:.2f}")
            st.write(f"- Product 2 per week: {product2_per_week:.2f}")
            st.write(f"- Product 3 per week: {product3_per_week:.2f}")

            st.subheader("**Month**")
            st.write(f"- Product 1 per month: {product1_per_month:.2f}")
            st.write(f"- Product 2 per month: {product2_per_month:.2f}")
            st.write(f"- Product 3 per month: {product3_per_month:.2f}")

            st.subheader("**All Project**")
            st.write(f"- All project Product 1: {product1_all:.2f}")
            st.write(f"- All project Product 2: {product2_all:.2f}")
            st.write(f"- All project Product 3: {product3_all:.2f}")

        st.subheader("Others")
        st.write("KPI for Others:")
        col3, col4 = st.columns(2)
        with col3:
            st.write(f"- KPI per day (others): {kpi_per_day_o:.2f} VND")
            st.write(f"- KPI per week (others): {kpi_per_week_o:.2f} VND")
            st.write(f"- KPI per month (others): {kpi_per_month_o:.2f} VND")
        with col4:
            st.subheader("**Week**")
            st.write(f"- Product 1 per week (others): {product1_per_week_o:.2f}")
            st.write(f"- Product 2 per week (others): {product2_per_week_o:.2f}")
            st.write(f"- Product 3 per week (others): {product3_per_week_o:.2f}")
    
            st.subheader("**Month**")
            st.write(f"- Product 1 per month (others): {product1_per_month_o:.2f}")
            st.write(f"- Product 2 per month (others): {product2_per_month_o:.2f}")
            st.write(f"- Product 3 per month (others): {product3_per_month_o:.2f}")
    
            st.subheader("**All Project**")
            st.write(f"- All project Product 1 (others): {product1_all_o:.2f}")
            st.write(f"- All project Product 2 (others): {product2_all_o:.2f}")
            st.write(f"- All project Product 3 (others): {product3_all_o:.2f}")


if __name__ == "__main__":
    run()

