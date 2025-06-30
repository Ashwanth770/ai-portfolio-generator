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
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

4. Run the application:

```bash
streamlit run Home.py
```

---


## How to run the website 

### Go to the Home page

![image](https://github.com/user-attachments/assets/9cb3355e-e29d-4a89-83cf-d8f05fe43cb6)

---

### Click on the Create button in sidebar and enter the details in the page
  
![image](https://github.com/user-attachments/assets/31c39591-f98a-421b-9bb8-0ed4eb2816f6)

---

### Add the profile picture and certificates or projects if any and click save

![image](https://github.com/user-attachments/assets/05f7e702-3777-4236-af46-488fda6eceaf)

---

### Now move to the generate page using sidebar to see the webpage preview
  
![image](https://github.com/user-attachments/assets/87d57d4e-48d6-4a55-b410-63275e0c3fc8)

---

### See the sample preview of the generated webpage and click on download zip to view the code and final portfolio
  
![image](https://github.com/user-attachments/assets/b7f4ed0d-97ab-4645-acb3-91cf01d97e63)

---

### Note that the whole webpage may not be seen in the preview so download and see the final webpage
  
![image](https://github.com/user-attachments/assets/10a4397d-8ae6-4fb4-a235-d552e2aec1f0)



