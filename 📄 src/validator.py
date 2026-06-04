from checks import is_noise, is_malformed, is_multilingual

def validate_transcript(text):
    
    if not text.strip():
        return {"status": "Invalid", "reason": "Empty Transcript"}
    
    if is_malformed(text):
        return {"status": "Invalid", "reason": "Malformed Text"}
    
    if is_noise(text):
        return {"status": "Invalid", "reason": "Noise Only"}
    
    if is_multilingual(text):
        return {"status": "Warning", "reason": "Multilingual Artifact"}
    
    return {"status": "Valid", "reason": "Clean Transcript"}
