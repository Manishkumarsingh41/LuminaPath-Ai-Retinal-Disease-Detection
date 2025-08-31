# LuminaPath - AI-Powered Retinal Disease Detection

**LuminaPath** is an AI-powered retinal disease detection system that helps medical practitioners detect and analyze retinal conditions from OCT (Optical Coherence Tomography) scans. The system provides automated predictions, confidence scores, and detailed explanations, all presented in professional PDF reports.

---

## MBP (Most Basic Purpose)

The core purpose of LuminaPath is to **automate retinal disease detection** and generate professional **PDF reports** for patient records. This helps doctors save time, improve accuracy, and provide clear AI explanations for detected conditions.

---

## Features

- **Retinal Scan Upload:** Drag & drop OCT images (jpg, jpeg, png)  
- **AI Prediction:** Detects retinal diseases like Diabetic Retinopathy with confidence score  
- **Multi-language Explanations:** Supports English, Hindi, Hinglish, Bhojpuri, Spanish, French, Chinese  
- **PDF Report Generation:** Includes
  - Patient information  
  - Uploaded retinal scan  
  - AI Prediction & Confidence  
  - Horizontal Confidence Bar  
  - AI Explanation (text-wrapped)  
  - Doctor’s Signature Placeholder  
- **Interactive Streamlit UI** with modern neumorphic design  
- **Auto-prediction** when generating PDF if not already run

---

## Demo Screenshot

![UI Screenshot](path_to_screenshot.png)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Manishkumarsingh41/LuminaPath-Ai-Retinal-Disease-Detection.git
cd LuminaPath


```
```bash 
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

```
```bash 

pip install -r requirements.txt
```

streamlit run frontend/app.py

```
## Project/File Structure
```
```bash

LuminaPath/
│
├── frontend/
│   ├── app.py                # Main Streamlit entry point
│   ├── components/
│   │   ├── upload_section.py # Upload & preview section
│   │   ├── prediction_view.py
│   │   ├── explanation_view.py
│   │   ├── report_download.py
│   │   └── language_selector.py
│   ├── assets/
│   │   ├── logo.png
│   │   └── styles.css
│   └── __init__.py
│
├── backend/
│   ├── api.py
│   ├── model_inference.py
│   ├── report_generator.py
│   └── __init__.py
│
├── models/
│   └── retinal_cnn_model.h5
│
├── data/
│   └── sample_images/
│
├── requirements.txt
└── README.md

```

## Future Improvements

Add hospital/clinic logo in the PDF reports

Support detection of multiple retinal diseases

Real-time webcam-based retinal scanning

Deploy as a web service or desktop application

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

## Manish Kumar Singh
GitHub: https://github.com/Manishkumarsingh41

Portfolio: https://iammanishsinghrajput.netlify.app/
