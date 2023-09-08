from fastapi import FastAPI, Query
from datetime import datetime, time, timedelta
import pytz

app = FastAPI()


@app.get("/")
async def root(slack_name: str = Query(""), track: str = Query("")):

    current_time = datetime.now(pytz.UTC)
    utc_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = current_time.strftime("%A")

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