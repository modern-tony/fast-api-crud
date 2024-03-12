from fastapi import FastAPI, HTTPException
from sentry_sdk import set_user
import sentry_sdk

set_user({"email": "jane.doe@example.com"})

sentry_sdk.init(
    dsn="https://805e38602c2ad49ae51c8d11fa7ad5dc@o4506899278856192.ingest.us.sentry.io/4506899280297984",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


app = FastAPI()


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

# create crud operations

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Simulate error condition
    if item_id == 999:  # Example condition
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if item_id == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(name: str):
    # Simulate error condition
    if name == "error":  # Example condition
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if name == "not found":
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": name}

@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str):
    # Simulate error condition
    if item_id == 999 or name == "error":  # Example condition
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if item_id == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_name": name, "item_id": item_id}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    # Simulate error condition
    if item_id == 999:  # Example condition
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if item_id == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

@app.get("/")
async def root():
    # Simulate error condition
    raise HTTPException(status_code=500, detail="Internal Server Error")
    