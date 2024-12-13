import requests

# login
def test_login(id:str,pw:str)->dict | None:
    response = requests.post("http://localhost:7777/login",data={"username":id,"password":pw})
    if response.status_code == 200:
        re_json = response.json()
        return re_json
    
    else:
        return None

# apikey get
def test_get_api_key(token:str)->dict | None:
    headers = {
        "Authorization":f"Bearer {token}"
    }
    response = requests.get("http://localhost:7777/get-api-key",headers=headers)
    if response.status_code == 200:
        re_json = response.json()
        return re_json
    
    else:
        return None
# auth api key
def test_auth_api_key(apikey:str,username:str)->bool:
    response = requests.post("http://localhost:7777/auth-api-key",data={"api_key":apikey,"username":username})
    if response.status_code == 200:
        re_json = response.json()
        return re_json
    else:
        return False

if __name__ == "__main__":
    data = test_login("admin1","qwer1234!@")
    print(data)
    api_key = test_get_api_key(data['token'])
    print(api_key)
    print(test_auth_api_key(**api_key))