import re
from langdetect import detect_langs

def is_noise(text):
    if len(set(text)) <= 2:
        return True
    if len(re.findall(r'[a-zA-Z]', text)) / max(len(text),1) < 0.3:
        return True
    return False

def is_malformed(text):
    try:
        text.encode('utf-8').decode('utf-8')
        return False
    except:
        return True

def is_multilingual(text):
    try:
        langs = detect_langs(text)
        return len(langs) > 1
    except:
        return False
