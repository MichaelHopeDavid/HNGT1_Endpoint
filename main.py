from fastapi import FastAPI, Query
from datetime import datetime, timedelta
import pytz

app = FastAPI()


@app.get("/api")
async def root(slack_name: str = Query(""), track: str = Query("")):

    current_day = datetime.utcnow().strftime("%A")
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    response_data = { 
    "slack_name": slack_name,
    "current_day": current_day,
    "utc_time": utc_time,
    "track": track,
    "github_file_url": "https://github.com/MichaelHopeDavid/HNGT1_Endpoint/blob/master/main.py",
    "github_repo_url": "https://github.com/MichaelHopeDavid/HNGT1_Endpoint/tree/master",
    "status_code": 200
    }

    return response_data


if __name__ == "__main__":
    import uvicorn