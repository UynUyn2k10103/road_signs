from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from models.predict import predict
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

IMAGEDIR = "static/"

tmp = 0
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    f = open(f"web/index.html", "r")
    html_code = f.read()
    return HTMLResponse(content=html_code, status_code=200)

@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):
    global tmp 
    tmp = abs(tmp-1)
    file.filename = f"predict{tmp}.png"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    item = predict(f"{IMAGEDIR}{file.filename}")

    json_compatible_item_data = jsonable_encoder(item)

    return JSONResponse(content=json_compatible_item_data)
