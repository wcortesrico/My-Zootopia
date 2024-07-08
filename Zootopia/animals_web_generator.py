import json
import requests



def requesting_from_API(animal_name):
    API_key = "VtRld3UBsabpn8hSPFL+LA==0LXUcUl6h8bwBRUI"
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_key})
    if response.status_code == requests.codes.ok:
        return (response.text)
    else:
        return "Error:", response.status_code, response.text

def writing_json_file(text_response):
    with open("animals_data.json", "w") as new_file:
        new_file.write(text_response)


def load_data(file_path):
    """"" loads json file"""
    with open(file_path, "r") as handle:
     return json.load(handle)

def serialize_animal(animal_obj):
    output = ''
    name = animal_obj['name']
    diet = animal_obj["characteristics"]["diet"]
    first_location = animal_obj["locations"][0]
    output += '\n<li class ="cards__item">\n'
    output += f'<div class="card__title"> {name}</div>\n'
    output += f'<p class="card__text">\n'
    output += "<ul>\n"
    output += f'<li><strong>Diet:</strong> {diet}</li>\n'
    output += f'<li><strong>Location:</strong> {first_location}</li>\n'
    if "type" in animal_obj["characteristics"]:
        fox_type = animal_obj["characteristics"]["type"]
        output += f'<li><strong>Type:</strong> {fox_type}</li>\n'
    if "color" in animal_obj["characteristics"]:
        color = animal_obj["characteristics"]["color"]
        output += f'<li><strong>Color:</strong> {color}</li>\n'
    output += '</ul>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output

def get_skin_type_list(animal_data):
    skin_type_list = []
    for animal_obj in animal_data:
        if "skin_type" in animal_obj["characteristics"]:
            if animal_obj["characteristics"]["skin_type"] not in skin_type_list:
                skin_type_list.append(animal_obj["characteristics"]["skin_type"])
        else:
            pass
    return skin_type_list

def main():
    text_request = requesting_from_API("dog")
    writing_json_file(text_request)

    animals_data = load_data("animals_data.json")
    print("Skin types: ")

    skin_type_list = get_skin_type_list(animals_data)

    for skin_type in skin_type_list:
        print("-", skin_type)
    bad_input = True
    while bad_input:
        skin_type_selected = input("Type one of the skin types from the list of top: ")
        if skin_type_selected in skin_type_list:
            bad_input = False
        else:
            print("Try again")

    output = ''
    for animal_obj in animals_data:
        try:
            if skin_type_selected == animal_obj['characteristics']['skin_type']:
                output += serialize_animal(animal_obj)
            else:
                pass
        except KeyError as e:
            pass

    with open("animals_template.html", "r") as data:
        animals_html = data.read()
        animals_html = animals_html.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as new_html:
        new_html.write(animals_html)

if __name__ == "__main__":
    main()



