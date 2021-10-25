import requests
import configparser
from isurveyAPI import ApiISurvey
#from pymongo import MongoClient


config = configparser.ConfigParser()
config.read('config.ini')

user = config['API_SURVEY']['USER']
password = config['API_SURVEY']['PASSWORD']
consulta = config['API_SURVEY']['CONSULTA']

api = ApiISurvey(user,password)
api.Authenticate()


def get_pessoa_by_email(email):
    print("abriu pessoa")
    result = api.get_pessoa_by_email(email)
    return result

# def get_participante_consulta(email):
#     result = consulta.find_one({"pessoa.email":email})
#     return result 
