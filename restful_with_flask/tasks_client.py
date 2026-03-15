import requests

SERVICE_HOST = 'localhost'
SERVICE_HOST_PORT='5000'
SERVICE_STUDENT_PATH = '/todo/api/tasks'

def get_endpoint():
    return 'http://'+ SERVICE_HOST+':'+SERVICE_HOST_PORT


def get_tasks():
    response = requests.get(get_endpoint()+SERVICE_STUDENT_PATH)
    if response.json:
        print(response.json())

def get_task(task_id):
    response = requests.get(get_endpoint()+SERVICE_STUDENT_PATH+'/'+str(task_id))
    if response.json:
        print(response.json())

print("------------------------------------") 
get_tasks()
print("------------------------------------") 
get_task(1)
print("------------------------------------") 