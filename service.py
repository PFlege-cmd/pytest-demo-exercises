import requests

class Service:
    def get_users(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        if response.status_code == 200:
            print(response.json())
            return response
