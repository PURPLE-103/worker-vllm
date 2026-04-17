import logging
import os


def load_chat_template_override():
    inline_template = os.getenv("CUSTOM_CHAT_TEMPLATE")
    file_path = os.getenv("CHAT_TEMPLATE")

    if file_path:
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        logging.warning(
            "CHAT_TEMPLATE=%s is not a readable file; falling back to CUSTOM_CHAT_TEMPLATE",
            file_path,
        )

    return inline_template
