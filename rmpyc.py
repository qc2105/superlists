from pathlib import Path

current_dir = Path('.')

for file_ in current_dir.glob('**/*.pyc'):
    file_.unlink()

current_dir = Path('.')

for file_ in current_dir.glob('**/__pycache__'):
    file_.rmdir()
