import os

LINE = ("Dear Management, I am writing to tender my resignation, effective immediately, "
        "because I have decided to pursue a career that better suits my talents, "
        "which after extensive self-assessment I have narrowed down to anything else.")

def main():
    line = LINE.strip().replace("\n", " ")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
