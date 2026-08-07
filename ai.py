from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def organize_menu(text):

    prompt = f"""
Extrage produsele din meniul de restaurant.

Reguli:
- Returneaza DOAR JSON valid.
- Nu scrie explicatii.
- Ignora titluri precum PIZZA, PASTE, BAUTURI.
- Fiecare produs trebuie sa aiba:
  - category
  - name
  - price

Format:

[
  {{
    "category": "Pizza",
    "name": "Pizza Margherita",
    "price": "35 lei"
  }}
]

Text:

{text}
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    print("AI RESPONSE:")
    print(content)

    # Scoate eventualele ```json
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        return json.loads(content)
    except Exception as e:
        print("JSON ERROR:", e)
        return []