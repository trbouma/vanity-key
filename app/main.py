from pathlib import Path
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Directory that contains index.html (project root: one level up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent

# Serve the whole folder as static, with index.html as the default document
# Visiting "/" will return your index.html automatically.
app.mount("/", StaticFiles(directory=BASE_DIR, html=True), name="static")
