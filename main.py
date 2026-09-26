from fastapi import FastAPI

app = FastAPI(title="Interview Question Generator")

@app.get("/")
def read_root():
    return {"message": "Hello World - Interview Question Generator API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
