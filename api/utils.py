import requests


def is_car_exist(make, model):

    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/\
    {make}?format=json'
    data = requests.get(url).json()['Results']
    return any(model == car['Model_Name'] for car in data)
