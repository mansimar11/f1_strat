import streamlit as st
from PIL import Image

st.set_page_config(page_title="Data Analytics", page_icon="📈", layout="wide")
st.title("Data Analytics Dashboard 📈")
st.info("This is the dedicated space for your embedded Power BI dashboard.")

# Show the dashboard image using the correct parameter
image = Image.open("F1_DASHBOARD.jpg")
st.image(image, caption="Visual Dashboard Preview", use_container_width=True)

# Provide PDF download button
pdf_path = "F1_DASHBOARD.pdf"
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

st.download_button(
    label="📄 Download PDF Dashboard",
    data=pdf_bytes,
    file_name="F1_DASHBOARD.pdf",
    mime="application/pdf"
)

# GitHub link
st.markdown("---")
st.markdown(
    """
    📂 The original `.pbix` file for this dashboard can be found on 
    [GitHub](https://github.com/mansimar11/f1_strat/blob/main/F1%20DASHBOARD.pbix).
    """
)
