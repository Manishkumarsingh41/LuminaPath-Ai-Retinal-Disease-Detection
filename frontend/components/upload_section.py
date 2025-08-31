import streamlit as st
from PIL import Image

def upload_section():
    st.title("🌌 LuminaPath: Retinal Disease Detection")
    st.write("Upload an **OCT image** to analyze and get AI-powered insights.")

    uploaded_file = st.file_uploader("📤 Upload your OCT Image", type=["jpg", "jpeg", "png", "tiff"])

    if uploaded_file is not None:
        # Open the image
        image = Image.open(uploaded_file)
        
        # Show preview
        st.image(image, caption="🖼️ Uploaded OCT Image", use_column_width=True)

        # Placeholder for predictions
        st.markdown("### 🔮 Prediction Result (Coming Soon...)")
        st.info("Once the AI model is integrated, you’ll see disease predictions and explanations here.")
    else:
        st.warning("Please upload an OCT image to proceed.")
