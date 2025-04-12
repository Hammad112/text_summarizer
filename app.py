from fastapi import FastAPI 
import uvicorn
import sys,os 
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response 
from src.text_summarizer.pipeline.prediction_pipeline import predictionPipeline


text:str ="What is Text Summarization"
app=FastAPI()

@app.get("/",tags=['authentication'])

async def index():
    return RedirectResponse(url='/docs')


@app.get('/train')
async def training():
    try:
        os.system('python main.py')
        return Response('Trained Successfully')
    except Exception as e:
        return Response(f'Error Ocurred {e}')


@app.post('/predict')
async def predict_route(text):
    try:
        obj=predictionPipeline()
        text=obj.predict(text)
        return text
    
    except Exception as e:
        raise e

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)