import requests

response = requests.get('http://api.open-notify.org/astros.json')
json_data = response.json()

number_of_people = json_data['number']
people_in_space = json_data['people']

print("There are", number_of_people, "people in space right now...")

for astronaut in people_in_space:
  print(astronaut['name'], "is on the following space craft:", astronaut['craft'])
