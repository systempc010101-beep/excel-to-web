import streamlit as st
import pandas as pd

st.title("📊 نمایش همه شیت‌های اکسل")

# آپلود فایل
uploaded_file = st.file_uploader("فایل اکسل را انتخاب کنید", type=["xlsx", "xls"])

if uploaded_file is not None:
    # گرفتن لیست شیت‌ها
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names

    st.success("✅ فایل آپلود شد. همه شیت‌ها در تب‌های زیر نمایش داده می‌شوند:")

    # ساختن تب‌ها بر اساس شیت‌ها
    tabs = st.tabs(sheet_names)

    for i, sheet in enumerate(sheet_names):
        with tabs[i]:
            st.subheader(f"📄 شیت: {sheet}")
            df = pd.read_excel(uploaded_file, sheet_name=sheet)
            st.dataframe(df)

else:
    st.warning("⚠️ هنوز فایلی آپلود نشده است")
