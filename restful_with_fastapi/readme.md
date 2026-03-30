# Environment configuration

## Linux

`python3 -m venv .venvFastAPI`

`source .venvFastAPI/bin/activate`

`pip install fastapi`

`pip install uvicorn`

Go to `restful_with_fastapi` folder and run `uvicorn tasks_fastapi_app:app`.

Go to http://localhost:8000/docs webpage to open the OpenAPI documentation of the service.

