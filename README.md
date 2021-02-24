# fastapi-url-shortener

Simple yet powerful URL shortener built with FastAPI.



- [fastapi-url-shortener](#fastapi-url-shortener)
  - [Docs](#docs)
  - [How to deploy](#how-to-deploy)
    - [Deploy to Heroku](#deploy-to-heroku)
    - [Run on Localhost](#run-on-localhost)

## Docs

- [Swagger UI](https://fastapi-url-shortener.herokuapp.com/docs)
- [Redoc](https://fastapi-url-shortener.herokuapp.com/redoc)

## How to deploy

You are expected to have `git` installed in your system.

First of all clone the repository and move into the directory.

  ```shell
  git clone https://github.com/aahnik/fastapi-url-shortener
  cd fastapi-url-shortener
  ```

### Deploy to Heroku

Make sure you have Heroku CLI installed.

- Create a new Heroku app
  ```shell
  heroku create
  ```

- Push the code to Heroku
  ```shell
  git push heroku main
  ```




### Run on Localhost
- Install dependancies from `requirements.txt`
  ```shell
  pip install -r requirements.txt
  ```
- Run the server using `uvicorn`
  ```shell
  uvicorn main:app --reload
  ```





