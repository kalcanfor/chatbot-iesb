import requests
import configparser
from isurveyAPI import ApiISurvey

config = configparser.ConfigParser()
config.read('config.ini')

user = config['API_SURVEY']['USER']
password = config['API_SURVEY']['PASSWORD']
consulta = config['API_SURVEY']['CONSULTA']

api = ApiISurvey(user,password)
api.Authenticate()


def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'get_pessoa':
        return_values = get_pessoa(parameters, return_var)
    # elif action == 'search':
    #     return_values = search_movies(parameters, return_var)
    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def get_pessoa(parameters, return_var):
    result_var = "O seu usuário não está cadastrado, faça seu cadastro pelo link http://isurvey.cgee.org.br/demo/cadastro para receber orientações em seu e-mail e gerar sua senha de acesso."
    email = parameters['email']
    print('Pesquisando por: ', email)
    result = api.get_pessoa_by_email(email)
    if(len(result)>0):
        print("result: ", result)
        if(len(result)==1):
            result_var = result[0]['nome']
        else:
            result_var = "mais de um participante foi encontrado!"
    else:
        print("Não encontrado!")
    
    return {
        return_var: result_var
    }
