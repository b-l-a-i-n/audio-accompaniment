import uvicorn
from fastapi import FastAPI, File, UploadFile
from utils import process_file_from_server
# App creation and model loading
app = FastAPI()


@app.post('/predict')
async def server_process(file: UploadFile = File(...)):
    json_predictions = await process_file_from_server(file)
    return json_predictions


if __name__ == '__main__':
    # Run server using given host and port
    uvicorn.run(app, host='127.0.0.1', port=80)
