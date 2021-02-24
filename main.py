from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import RedirectResponse, Response
from fastapi.templating import Jinja2Templates


app = FastAPI(title="fastapi-url-shortener")
templates = Jinja2Templates(directory='templates')

db = {}


class ShortUrl(BaseModel):
    slug: str
    url: str


@app.get('/')
def index(request: Request):

    return templates.TemplateResponse('index.html',
                                      context={'request': request},
                                      status_code=200)


@app.post('/shorten')
def shorten(sh: ShortUrl):
    db[sh.slug] = sh.url
    return Response(content='Success', status_code=201)


@app.get('/{slug}')
def redirect(slug: str, request: Request):
    print(slug)
    if slug in db:
        return RedirectResponse(url=db[slug])
    else:
        return templates.TemplateResponse('404.html',
                                          context={'request': request},
                                          status_code=404)
