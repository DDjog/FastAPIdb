import fastapi
import uvicorn
from src.routes import contacts

app = fastapi.FastAPI()
   

app.include_router(contacts.router, prefix='/api')


@app.get("/")
async def root():
    return {"message": "--> FastAPI contacts  <--"}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    