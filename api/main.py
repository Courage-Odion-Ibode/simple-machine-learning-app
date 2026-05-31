""""
This is the main file for the API. It imports the FastAPI library and creates an instance of the FastAPI class. The app is given a name "Machine Learning API". A single endpoint is defined at the root URL ("/") that returns a welcome message and the version of the API when accessed via a GET request.
The app is then run using the uvicorn server. The app will be available at http://localhost:8000/.
"""

from fastapi import FastAPI
from handler import Handler, InputData

app = FastAPI(name= "Machine Learning API")
handler = Handler()
handler.load_model()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Machine Learning API!", "version": "1.0.0"}

@app.get("/predict")
def predict_get():
   return {"message": "Please use a POST request to get predictions. Running Sucessfully!"}

@app.post("/predict")
def predict(input_data: InputData):
    prediction = handler.predict(input_data)
    return {"prediction": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)