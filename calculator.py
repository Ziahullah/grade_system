from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
def add(a: float, b: float):
    return {"operation": "add", "result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtract", "result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiply", "result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"operation": "divide", "result": a / b}