from typing import Optional
from fastapi import FastAPI, File, UploadFile
import uvicorn
from recipe import Recipe # ASGI it gets it faster
from predict import get_recipe_class

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# this must recive an image
@app.post("/predict")
def get_recipe_class(data: Recipe):
    data = data.dict()
    id = data['id']
    class_name = get_recipe_class(id)
    return class_name


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    

    print('file.filename', file.filename)
    return {"filename": file.filename}


# Run api with uvicorn
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=6000)


# Requires a post so I used fastapi docs
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


# # Run api with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


# uvicorn main:app --reload
