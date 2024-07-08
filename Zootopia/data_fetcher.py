import requests
def fetch_data(animal_name):
    API_key = "VtRld3UBsabpn8hSPFL+LA==0LXUcUl6h8bwBRUI"
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_key})
    if response.status_code == requests.codes.ok:
        return (response.text)
    else:
        return "Error:", response.status_code, response.text