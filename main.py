from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/check-ai")
def check_ai(text_to_ai: str = Query(...), word_to_check: str = Query(...)):
    ai_text = f"Simulated AI response for: {text_to_ai}"
    contains_word = word_to_check in ai_text
    return {"ai_response": ai_text, "contains_word": contains_word}
