# untuk me load atau untuk mengeluarkan dan melakukan validasi env

from dotenv import load_dotenv

load_dotenv()

import os

def _required_env(name: str) -> str:
    """Ambil env wajib. Apabila gagal, tampilkan pesan error"""

    value = os.getenv(name)

    if not value:
        raise RuntimeError()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")