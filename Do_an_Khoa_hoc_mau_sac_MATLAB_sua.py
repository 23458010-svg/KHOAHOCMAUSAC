
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Khoa học màu sắc HCMUTE",
    page_icon="🎨",
    layout="wide"
)

st.title("KHOA HỌC MÀU SẮC")
st.write("Ứng dụng Python và Streamlit chạy trên localhost")

st.sidebar.title("Danh mục chức năng")
page = st.sidebar.selectbox(
    "Chọn chức năng",
    [
        "Trang chủ",
        "Chuyển đổi sRGB sang XYZ",
        "Biểu đồ CIE",
        "So sánh CIELAB"
    ]
)

if page == "Trang chủ":
    st.header("Đề tài khoa học màu sắc")
    st.write("Sinh viên: NGÔ THANH LỘC")
    st.write("MSSV: 23458010")

elif page == "Chuyển đổi sRGB sang XYZ":
    r = st.number_input("R", 0, 255, 255)
    g = st.number_input("G", 0, 255, 0)
    b = st.number_input("B", 0, 255, 0)

    rgb = np.array([r, g, b]) / 255
    linear = np.where(
        rgb <= 0.04045,
        rgb / 12.92,
        ((rgb + 0.055) / 1.055) ** 2.4
    )

    matrix = np.array([
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041]
    ])

    xyz = matrix @ linear * 100

    st.subheader("Kết quả XYZ")
    st.write(f"X = {xyz[0]:.4f}")
    st.write(f"Y = {xyz[1]:.4f}")
    st.write(f"Z = {xyz[2]:.4f}")

elif page == "Biểu đồ CIE":
    st.info(
        "Phần biểu đồ CIE sẽ sử dụng dữ liệu "
        "CMF từ thư viện colour-science."
    )

elif page == "So sánh CIELAB":
    st.info(
        "Nhập Lab1 và Lab2 để phân tích "
        "độ sáng và hướng dịch chuyển màu."
    )
