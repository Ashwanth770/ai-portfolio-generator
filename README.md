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

<br/> <br/>

***Note: If the app is inactive please click get this app back***

![image](https://github.com/user-attachments/assets/d6d02c28-e844-403c-a554-3021205bcfca)

---

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
  
![image](https://github.com/user-attachments/assets/f3dc4032-b658-4a40-8a49-2dbd05ce58c4)

---

### See the sample preview of the generated webpage and click on download zip to view the code and final portfolio
  
![image](https://github.com/user-attachments/assets/edd3625b-2949-4499-9262-af202eab8040)

---

### Note that the whole webpage may not be seen in the preview so download to see the final webpage
  
![image](https://github.com/user-attachments/assets/b76079ad-f0c3-44e5-b998-58e1e07a4d20)

---

## Code Screenshot

### Home.py

![image](https://github.com/user-attachments/assets/ef737f6b-5775-444a-beaf-5bb6dfbaef98)

---

### 1_Create.py

![image](https://github.com/user-attachments/assets/61b9c798-4993-441f-8ff8-7e0846d7d68e)

---

### 2_Generate.py

![image](https://github.com/user-attachments/assets/7cc465b5-6502-45da-9aad-b9cbfa19dd82) <br/> <br/>

![image](https://github.com/user-attachments/assets/08f68976-ab5f-4b11-a975-2c14525cd5fb)

---

### utils.py

![image](https://github.com/user-attachments/assets/87963b7f-0701-489c-b65c-36a1d01cfc12)









