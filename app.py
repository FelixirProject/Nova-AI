import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

SYSTEM_PROMPT = (
    "Kamu adalah NOVA, asisten AI yang ramah, cerdas, dan membantu. "
    "Jawab dalam Bahasa Indonesia kecuali pengguna meminta bahasa lain. "
    "Jelaskan dengan jelas dan sesuaikan tingkat penjelasan dengan pertanyaan."
)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return jsonify({"error": "GROQ_API_KEY belum diatur. Isi file .env terlebih dahulu."}), 500

    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])

    if not isinstance(messages, list) or not messages:
        return jsonify({"error": "Pesan tidak boleh kosong."}), 400

    # Batasi jumlah dan ukuran pesan yang dikirim ke API.
    safe_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for item in messages[-20:]:
        if not isinstance(item, dict):
            continue
        role = item.get("role")
        content = item.get("content")
        if role not in ("user", "assistant") or not isinstance(content, str):
            continue
        content = content.strip()[:6000]
        if content:
            safe_messages.append({"role": role, "content": content})

    if len(safe_messages) == 1:
        return jsonify({"error": "Pesan tidak valid."}), 400

    try:
        client = Groq(api_key=api_key)
        result = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            messages=safe_messages,
            temperature=0.7,
            max_completion_tokens=1200,
        )
        answer = result.choices[0].message.content or "Maaf, aku belum bisa membuat jawaban."
        return jsonify({"reply": answer})
    except Exception as exc:
        # Jangan kirim detail rahasia/API key ke browser.
        print("Groq API error:", repr(exc))
        return jsonify({"error": "AI sedang mengalami kendala. Periksa API key, koneksi internet, dan model di file .env."}), 502

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
