NOVA AI CHAT — CARA MENJALANKAN

1. Ekstrak file ZIP ini.
2. Buka folder nova_ai_chat di VS Code.
3. Buka Terminal di folder tersebut.
4. Buat virtual environment (opsional tetapi disarankan):
   python -m venv .venv

   Windows:
   .venv\Scripts\activate

   Mac/Linux:
   source .venv/bin/activate

5. Install library:
   pip install -r requirements.txt

6. Salin file .env.example menjadi .env.
   Isi GROQ_API_KEY dengan API key Groq milikmu.
   Jangan pernah membagikan file .env atau memasukkan API key ke HTML/JavaScript.

7. Jalankan:
   python app.py

8. Buka browser:
   http://127.0.0.1:5000

CATATAN
- Website ini adalah versi awal: chat teks dengan riwayat percakapan selama halaman dibuka.
- API key diproses di backend Python, bukan di browser.
- Untuk dipublikasikan ke internet, perlu hosting backend dan konfigurasi keamanan tambahan.
- Model dapat diganti melalui GROQ_MODEL di file .env jika model pilihanmu tersedia di akun Groq.


PUBLISH TO INTERNET (PHONE ONLY)
A. Create a GitHub repository and upload the CONTENTS of this folder (not the ZIP itself). Do not upload .env or any real API key.
B. On Render, create a new Web Service and connect that repository.
C. Set: Language = Python 3; Build Command = pip install -r requirements.txt; Start Command = gunicorn app:app --bind 0.0.0.0:$PORT
D. In Environment Variables, add GROQ_API_KEY with your private Groq key and GROQ_MODEL with llama-3.3-70b-versatile.
E. Deploy and open the public onrender.com address. Free services may sleep after inactivity and take time to wake.

Keep the API key private. Never paste it into index.html, screenshots, public repositories, or chat messages.
