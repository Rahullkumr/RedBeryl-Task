from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Create directories if not exist
os.makedirs("documents", exist_ok=True)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})


@app.post("/upload")
async def upload_file(docType: str = Form(...), file: UploadFile = File(...)):
    # Save the uploaded file in the documents folder
    file_location = f"documents/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {"message": f"File uploaded successfully as {docType}"}
