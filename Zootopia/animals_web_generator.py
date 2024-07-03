import json
def load_data(file_path):
    """"" loads json file"""
    with open(file_path, "r") as handle:
     return json.load(handle)


animals_data = load_data("animals_data.json")

output = ""
for fox_info_dictionary in animals_data:
    name = fox_info_dictionary["name"]
    diet = fox_info_dictionary["characteristics"]["diet"]
    first_location = fox_info_dictionary["locations"][0]
    output += f"\n\nName: {name}\nDiet: {diet}\nLocation: {first_location}"
    if "type" in fox_info_dictionary["characteristics"]:
        fox_type = fox_info_dictionary["characteristics"]["type"]
        output += f"Type: {fox_type}"
#print(output)

with open("animals_template.html", "r") as data:
    animals_html = data.read()
    animals_html = animals_html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as new_html:
    new_html.write(animals_html)



