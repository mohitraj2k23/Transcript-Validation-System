from src.validator import validate_transcript

def test_cases():
    samples = [
        "",
        "aaaaaaa",
        "@@@###",
        "Hello world",
        "���",
        "Hello नमस्ते"
    ]

    for text in samples:
        print(text, "→", validate_transcript(text))

if __name__ == "__main__":
    test_cases()
