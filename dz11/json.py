import requests
json_data = requests.get('https://jsonplaceholder.typicode.com/posts')
json_data = json_data.json()
s = str()
for i in json_data:
    s+=("Title: " + str(i['title'].replace("\n", ".\n").capitalize()) +".\n")
    s+=("Body: " + str(i['body'].replace("\n", ".\n").capitalize())+ ".\n\n")

sentences = s.split('\n')
final_sentences = []

for sentence in sentences:
    sentence = sentence.strip()
    sentence = sentence.capitalize()
    final_sentences.append(sentence)
    final_text = '\n'.join(final_sentences)

with open("json.txt", 'w') as file:
    file.writelines(final_text)
