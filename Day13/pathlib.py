from pathlib import Path

folder = Path("data")
file_path = folder / "info.txt"

folder.mkdir(exist_ok=True)

file_path.write_text("Hello Pathlib....", encoding="utf-8")