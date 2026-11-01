
import streamlit as st

st.set_page_config(
    page_title="Khoa học Màu sắc HCMUTE",
    layout="wide"
)


# 2. Căn giữa logo trường HCMUTE
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        "B_Tagline - HCM-UTE -.png",
        width=600
    )


# 3. Tiêu đề và thông tin sinh viên
st.markdown(
    "<h3 style='text-align: center;'>"
    "Chào mừng bạn đến với project Khoa học Màu sắc của mình!"
    "</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center;'>"
    "Mình tên là NGÔ THANH LỘC"
    "</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center;'>"
    "MSSV 23458010"
    "</h1>",
    unsafe_allow_html=True
)
