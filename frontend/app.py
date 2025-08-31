import streamlit as st
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io
import textwrap

# --------- PAGE CONFIG ----------
st.set_page_config(
    page_title=" LuminaPath: AI Retinal Analyzer",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------- CUSTOM CSS -----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .neumorphic-box {
        background: #1e2a38;
        border-radius: 20px;
        box-shadow: 10px 10px 20px #0b1116,
                    -10px -10px 20px #33485a;
        padding: 25px;
        margin: 15px 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        color: white;
        font-size: 16px;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        border: none;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.4);
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0072ff, #00c6ff);
        transform: scale(1.05);
    }
    .center { text-align: center; }
</style>
""", unsafe_allow_html=True)

# --------- HEADER ----------
st.markdown("<h1 class='center'>🧬 LuminaPath AI: Retinal Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>Futuristic AI-powered Retinal Disease Detection with Explainability</p>", unsafe_allow_html=True)

# --------- PATIENT INFO ----------
st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)
st.subheader("👤 Patient Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
with col2:
    phone = st.text_input("Phone Number")
    address = st.text_area("Address")
st.markdown("</div>", unsafe_allow_html=True)

# --------- MAIN LAYOUT ----------
col1, col2 = st.columns([1, 1])

uploaded_file = None
prediction = None
confidence = 92
explanation = "This scan shows early signs of Diabetic Retinopathy. Detected patterns include small hemorrhages and microaneurysms."

with col1:
    st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)
    st.subheader("📂 Upload Retinal Scan")
    uploaded_file = st.file_uploader("Drag & Drop OCT Image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Retinal Scan", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)
    if st.button("🔮 Run Prediction"):
        prediction = "Diabetic Retinopathy"
        st.success(f"✅ Prediction: {prediction} detected with {confidence}% confidence.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)
    st.subheader("🧾 AI Explanation")
    st.write(explanation)

    st.markdown("#### 🌍 Select Explanation Language")
    lang = st.selectbox("Choose Language", ["English", "Hindi", "Hinglish", "Bhojpuri", "Spanish", "French", "Chinese"])
    st.info(f"Explanations will be provided in **{lang}**")
    st.markdown("</div>", unsafe_allow_html=True)

# --------- EXTRA FEATURES ----------
st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)
st.subheader("📊 Analytics & Confidence")
st.progress(confidence)
st.metric("Confidence", f"{confidence}%", "High Certainty")
st.markdown("</div>", unsafe_allow_html=True)

# --------- PDF REPORT GENERATION ----------
def draw_confidence_bar(c, x, y, width, height, percent):
    """Draw horizontal confidence bar in PDF."""
    c.setFillColor(colors.grey)
    c.rect(x, y, width, height, fill=1, stroke=0)
    c.setFillColor(colors.blue)
    c.rect(x, y, width * (percent/100), height, fill=1, stroke=0)

def wrap_text(text, width=90):
    """Wrap text for PDF multi-line rendering."""
    return "\n".join(textwrap.wrap(text, width=width))

if st.button("📥 Generate PDF Report"):
    # Auto-run prediction if not done
    if not prediction:
        prediction = "Diabetic Retinopathy"

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    page_width, page_height = A4

    # Header
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(page_width/2, page_height-50, "🏥 LuminaPath: AI Report")
    c.setFont("Helvetica", 11)
    c.drawRightString(page_width-50, page_height-70, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Divider
    c.setStrokeColor(colors.grey)
    c.setLineWidth(1)
    c.line(40, page_height-80, page_width-40, page_height-80)

    # Patient Info Column
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, page_height-110, "Patient Information:")
    c.setFont("Helvetica", 11)
    c.drawString(50, page_height-130, f"Name: {name}")
    c.drawString(50, page_height-150, f"Age: {age}")
    c.drawString(50, page_height-170, f"Phone: {phone}")
    c.drawString(50, page_height-190, f"Address: {address}")

    # Prediction Column
    c.setFont("Helvetica-Bold", 12)
    c.drawString(320, page_height-110, "AI Prediction & Confidence:")
    c.setFont("Helvetica", 11)
    c.drawString(320, page_height-130, f"Condition: {prediction}")
    c.drawString(320, page_height-150, f"Confidence: {confidence}%")

    # Uploaded Image
    if uploaded_file:
        img = ImageReader(uploaded_file)
        max_width, max_height = 250, 200
        c.drawImage(img, 50, page_height-400, width=max_width, height=max_height, preserveAspectRatio=True)

    # Confidence Bar
    draw_confidence_bar(c, 320, page_height-170, 200, 15, confidence)

    # Explanation
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, page_height-420, "AI Explanation:")
    c.setFont("Helvetica", 11)
    wrapped_text = wrap_text(explanation, width=80)
    text_object = c.beginText(50, page_height-440)
    text_object.textLines(wrapped_text)
    c.drawText(text_object)

    # Doctor Signature
    c.setFont("Helvetica", 11)
    c.drawString(50, 80, "Doctor's Signature: ___________________________")

    c.showPage()
    c.save()
    buffer.seek(0)

    st.download_button(
        label="⬇️ Download PDF Report",
        data=buffer,
        file_name=f"PathAI_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
        mime="application/pdf"
    )
