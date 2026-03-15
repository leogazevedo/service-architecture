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

def post_task(title, description):
    task_in_json = {
        'title' : title,
        'description' : description
    }
    response = requests.post(get_endpoint()+SERVICE_STUDENT_PATH,json=task_in_json)
    if response.json:
        print(response.json())

def put_task(id, title, description):
    task_in_json = {
        'title' : title,
        'description' : description
    }
    response = requests.put(get_endpoint() + SERVICE_STUDENT_PATH +'/' + str(id), json=task_in_json)
    if response.json:
        print(response.json())

def delete_task(id):
    response = requests.delete(get_endpoint() + SERVICE_STUDENT_PATH +'/' + str(id))
    if response.json:
        print(response.json())

print("==>POST---------------------------------") 
post_task('Test the web service','You should test the web service considering all possible invocations.')
print("==>GET------------------------------------") 
get_tasks()
print("==>PUT------------------------------------") 
put_task(3,'Test web service X', 'You should test this web service.')
print("==>DELETE------------------------------------") 
delete_task(3)
