from fastapi import FastAPI
from datetime import datetime, time, timedelta
import pytz

app = FastAPI()


@app.get('/')
async def root():

    current_time = datetime.now(pytz.UTC)
    utc_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = current_time.strftime("%A")

    response_data = { 
  "slack_name": "Michaelson",
  "current_day": current_day,
  "utc_time": utc_time,
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
    }

    return response_data