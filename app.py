# app.py

from fastapi import FastAPI
from routers import machinery_router, client_router, contract_router, payment_router

app = FastAPI()

# Include routers
app.include_router(machinery_router.router)
app.include_router(client_router.router)
app.include_router(contract_router.router)
app.include_router(payment_router.router)

@app.get("/")
def index():
    return app.openapi()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
