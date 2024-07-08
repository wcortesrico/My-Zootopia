import requests
API_key = "VtRld3UBsabpn8hSPFL+LA==0LXUcUl6h8bwBRUI"

def requesting_from_API(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_key})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return "Error:", response.status_code, response.text


def writing_json_file(json_response):
    with open("animals_datadfr.json", "w") as new_file:
        return new_file.write(json_response)

data = requesting_from_API("fox")

writing_json_file(data)