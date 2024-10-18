import requests
import json


def getAllProduto():
    res = requests.get("https://wiuhi.pythonanywhere.com/")    
    date = res.json()
    return date  


def save(name: str, amount: int, desc: str, image: str, price: float, category: str):
    url = "https://wiuhi.pythonanywhere.com/produtos/add"    
    dados = {'amount': amount, 'desc': desc, 'image': image, 'name': name, 'price': price, 'category': category, 'evaluation': 0}
    data_json = json.dumps(dados)
    headers={"Content-Type": "application/json"}
    response = requests.post(url, data=data_json, headers=headers)
    
    if response.status_code == 200:
        print("sucesso!")
    else:
        print("Erro", response.text)

