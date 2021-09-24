# lgf-fullstack-evaluation

#Looking Glass Factory Take Home Code Test Response

Response to the Looking Glass Factory Fullstack Evaluation

## Setup

####Dev Dependencies:
 - pyenv: [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
 - poetry: [https://python-poetry.org/](https://python-poetry.org/)
 - docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

####Usage:

#####To make a local dev environment:

    > cd lgf-fullstack-evaluation
    > pyenv install
    > poetry install


#####To run tests:

    > cd lgf-fullstack-evaluation
    > cd app/test
    > pytest -v *


#####To run server locally:

    > cd lgf-fullstack-evaluation
    > uvicorn app.main:app


default uvicorn serves at `http://127.0.0.1:8000`


#####To run server in a docker container:

    > cd lgf-fullstack-evaluation
    > docker-compose up


default gunicorn serves at `http://0.0.0.0`


#####Urls

api endpoint is:

* `get /v1/list`
* `post /v1/list_item/:list_item_id`

api swagger docs are at:

* `/docs`

#####Postman Collection

the postman collection has some simple requests to the end points
`lgf-fullstack-evaluation/LGF Fullstack Evaluation.postman_collection.json`

