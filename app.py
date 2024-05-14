# app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import machinery_router, client_router, contract_router, payment_router


app = FastAPI()

# Set up CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
