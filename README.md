# AI-Based Portfolio Generator using Streamlit and Gemini

This project is a Generative AI-powered tool that allows users to create a fully responsive and downloadable personal portfolio website. It uses the **Google Gemini API** to generate HTML code based on user inputs and provides a seamless interface built with **Streamlit**.

---

## Project Overview

The goal of this project is to simplify portfolio website creation using Generative AI. Users can:

- Enter their personal details (name, role, bio, skills, etc.)
- Upload profile pictures, project images, and certificates (images or PDFs)
- Preview the generated portfolio website
- Download the website as a single-page HTML zip

No coding knowledge is required for users to build and download their portfolio.

---

## Features

- Uses **Google Gemini API** to generate HTML dynamically
- Collects structured data via a clean Streamlit form
- Supports uploads of images and certificates
- All media embedded directly into the HTML via base64
- Sidebar layout with profile and media display
- Responsive and mobile-friendly design
- Real-time preview and downloadable `.zip` output
- Deployed on **Streamlit Cloud**

---

## Live Demo

Deployed on Streamlit Cloud:  
**https://ai-portfolio-generator-drf2lappdvtap8vqwhslfob.streamlit.app/**  

---

## Tech Stack

- Python
- Streamlit
- Google Generative AI (Gemini API)
- HTML + Inline CSS (generated)
- Base64 encoding (for embedding images and files)

---

## Installation

To run the project locally:

1. Clone the repository:
  
```bash 
git clone https://github.com/Ashwanth770/ai-portfolio-generator.git
cd ai-portfolio-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure Gemini API:

In .env replace with your api key
```bash
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

4. Run the application:

```bash
streamlit run Home.py
```


