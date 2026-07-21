# Menyimpan cara untuk melakukan konversi tulisan atau jawaban dari AI ke dalam bentuk markdown yang dikenali oleh telepon

import telegramify_markdown

def to_telegram_markdown(text: str) -> str:
    """Ubah markdown standard (output dari LLM) menjadi Telegram MarkdownV2 yang valid."""
    return telegramify_markdown.markdownify(text)
