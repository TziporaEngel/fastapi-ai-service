from fastapi import FastAPI, Query
import requests

app = FastAPI()

OPENAI_API_KEY = "YOUR_OPENAI_KEY"  # יש להחליף במפתח האמיתי

@app.get("/check-ai")
def check_ai(text_to_ai: str = Query(...), word_to_check: str = Query(...)):
        response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4",
            "messages": [{"role": "user", "content": text_to_ai}]
        }
    )

    ai_text = response.json()["choices"][0]["message"]["content"]

    contains_word = word_to_check in ai_text

    return {"ai_response": ai_text, "contains_word": contains_word}
