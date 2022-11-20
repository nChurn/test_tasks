from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/url_name/")
async def hello_view(name: str =None, message: str=None):
    if not name:
        return HTTPException(status_code=400, detail="Name must be set")
    if not message:
        return HTTPException(status_code=400, detail="Message must be set")
    return f"Hello {name}! {message}!"