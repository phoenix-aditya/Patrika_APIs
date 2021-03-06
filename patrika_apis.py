from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from starlette.responses import FileResponse

# custom file filters
from cussword_filter_dependencies.filters import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# landing page
@app.get("/")
def index():
    return FileResponse("landing_page/index.html")
    # return {"landing page":"here"}

# cussword filter API
@app.get("/cussword-filter/{article}")
def filter_article(article : str):
    final_str = replace_with_strike(article)
    return {
            "status":"pass",
            "filtered-text":final_str
        }

# use command pip list --format=freeze > requirements.txt
# to make the conda based requirements.txt file

if __name__ == "__main__":
    uvicorn.run(app, host="*")