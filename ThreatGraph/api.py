from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "ThreatGraph Running"
    }

@app.get("/assets")
def assets():
    return {
        "hostname": "api.example.com",
        "ip": "1.2.3.4"
    }
