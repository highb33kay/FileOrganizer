from pathlib import Path

entries = Path("C:\\Users\\HighB33Kay\\Desktop\\sort")

for entry in entries.iterdir():
    if entry.is_file():
        