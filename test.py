from pathlib import Path

entries = Path("C:\\Users\\HighB33Kay\\Desktop\\sort")

for entry in entries.iterdir():
    if entry.is_file():
        name = entry.stem
        ext = entry.suffix[1:]
        Path(Path("out")/ext).mkdir(parents=True, exist_ok=True)
        
        
