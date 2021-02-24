from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import RedirectResponse, Response

app = FastAPI(title="fastapi-url-shortener")


db = {}

class ShortUrl(BaseModel):
    slug: str
    url: str

@app.get('/')
def index():
    return Response(content='Server is up and running',status_code=200)

@app.post('/shorten')
def shorten(sh:ShortUrl):
    db[sh.slug] = sh.url
    return Response(content='Success',status_code=201)

@app.get('/{slug}')
def redirect(slug:str):
    if slug in db:
        return RedirectResponse(url=db[slug])
    else:
        return Response(status_code=404)

