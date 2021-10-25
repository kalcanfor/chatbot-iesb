import requests
import json
import pandas as pd
from unicodedata import normalize
import base64

class ApiISurvey:
    
    def __init__(self, username, password):
        self.urltoken = "http://portalh.cgee.org.br:6443/cas/v1/tickets?service=https://isurvey.cgee.org.br/iSurveyConfigurador/"
        self.payload = {
            "username": username,
            "password": base64.b64decode(password),
            "token": True
        }
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.headersAuth = ""
    
    def Authenticate(self):
        result = False
        response = requests.request("POST", self.urltoken, headers=self.headers, data=self.payload, verify=False)
        if(response.status_code==201):
            self.headersAuth = {
                "X-Access-Token": response.text
            }
        else:
            print(response)
        return(self.headersAuth)
    
    def get_pessoa_by_email(self, email):
        endpoint_buscaPessoa = "https://isurvey.cgee.org.br/iSurveyConfApi/api/configurador/v1/secure/buscaPessoa?page=0&pageSize=10&filter="+str(email)
        result = requests.request("GET", endpoint_buscaPessoa, headers=self.headersAuth, verify=False)
        if(result.status_code == 200):
            data = result.json()
        else:
            print("Response: ", result.status_code)
            print("Error: ",result.text)
            data = []        
        return(data)
        