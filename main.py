from fastapi import FastAPI
from router.router import libro

app = FastAPI()

app.include_router(libro)