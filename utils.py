import base64
import zipfile
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_portfolio_html(prompt):
    response = model.generate_content(prompt)
    return response.text

def zip_html_file(html_content, file_name="portfolio.html"):
    zip_path = "portfolio.zip"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_content)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(file_name)
    return zip_path
