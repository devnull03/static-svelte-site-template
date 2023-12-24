import json, os

tries_json = []

for i in range(1, 6):
	with open(f'questions/try{i}.json') as file:
		tries_json = [*tries_json, *json.loads(file.read())]

unique_json: dict = []

for i in range(len(tries_json)):
	# print(unique_json)
	if not len([*filter(lambda x: str(x) == str(tries_json[i]), unique_json)]):
		# print(tries_json[i], '\n')
		unique_json.append(tries_json[i])

print(len(unique_json))

with open('unique.json', 'w') as file:
	json.dump(unique_json, file)
