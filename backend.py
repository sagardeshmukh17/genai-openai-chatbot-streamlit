from http import client

from openai import OpenAI, api_key
from dotenv import load_dotenv
import os

# =============================
# Load environment variables
# =============================

load_dotenv()

# =============================
# Read OpenAI API key
# =============================

api_key = os.getenv("OPEN_AI_SECRET_KEY")

# ========================
# create OpenAI client
# ========================
client = OpenAI(api_key=api_key)


# ==========================
# function to call GPT model
# ==========================

def ask_gpt(model, prompt):
  response =  client.responses.create(
        model = model,
        input = prompt
    )

  return response.output_text
