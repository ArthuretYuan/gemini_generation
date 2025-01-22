import google.generativeai as genai
import getpass
import os

os.environ["GEMINI_API_KEY"] = getpass.getpass("Enter API key for GEMINI: ")
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)