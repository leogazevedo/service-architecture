# Environment configuration

## Linux

`python3 -m venv .venvFastAPI`

`source .venvFastAPI/bin/activate`

`pip install fastapi`

`pip install uvicorn`

Go to `restful_with_fastapi` folder and run `uvicorn tasks_fastapi_app:app --reload`.

Go to http://localhost:8000/docs webpage to open the OpenAPI documentation of the service.

To run the service using VS Code, add the following configuration in the debugger configuration, e.g., through configuring this file or adding this entry in the file `.vscode/launch.json`):

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "restful_with_fastapi.tasks_fastapi_app:app",
                "--reload"
            ],
            "jinja": true
        }
    ]
}
```
