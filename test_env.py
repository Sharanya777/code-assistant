from dotenv import load_dotenv
import os

load_dotenv()

print("Loaded key:", os.getenv("GEMINI_API_KEY"))
