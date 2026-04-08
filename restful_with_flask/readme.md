# Environment configuration

## Linux

To configure the environment:

`python3 -m venv .venvFlask`

`source .venvFlask/bin/activate`

`pip install flask`

To execute the micro-service on flask server in dev mode:

`python3 tasks_app.py` 

To execute the client applications:

`python3 tasks_client.py`

`python3 tasks_client_all_methods.py `

## restclient

- You can use restclient ([httpyac](https://httpyac.github.io/)) to test your endpoints. 
  - [VS Code Installation](https://httpyac.github.io/guide/installation_vscode.html)