def read_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def write_text(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
