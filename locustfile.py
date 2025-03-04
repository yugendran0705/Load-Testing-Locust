from locust import HttpUser, task
import random
import requests
import os
from dotenv import load_dotenv
load_dotenv()
# users=[]
# for i in requests.get("http://localhost:8080/api/user",
#                       headers={"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWdubyI6MTI1MTU2MTQ0LCJpYXQiOjE3MTYzOTcxOTR9.CQksCo7SM9iz9svQQEMHkknHoQTfuo5dp4QPWpptjV4"},
#                         ).json()['data']:
#     users.append(i['regno'])

token = os.getenv("TOKEN")

class MyUser(HttpUser):
    @task
    def createTicket(self):

        regno = random.randint(100000000, 100005000)
        phone = random.randint(6000000000, 9999999999)

        self.client.post(url="/api/user",
                        json={
                            "regno":regno, 
                            "name": "Yugendran", 
                            "mobile":phone,
                            "email":str(regno)+"@sastra.ac.in",
                            "department":"CSE", 
                            "year":1, 
                            "ishosteller": True, 
                            "gender":"Male",
                            "role":"USER"
                        }
        )
        # regno = random.choice(users)
        # regno = random.randint(100000000, 100005000)
        self.client.post(url="/api/ticket",
                        headers={"Authorization":"Bearer {token}"},
                        json={
                            "userId": regno, 
                            "eventId":1,
                            "answerList":[
                                {
                                    "answer":"hi da",
                                    "questionId":1
                                }
                            ]
                        }
                        )
        