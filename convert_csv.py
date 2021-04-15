import pandas as pd
import json
from addict import Dict

diretorio = './Jsons'
json_list = []
with open("%s/%s" % (diretorio, "acervo_1556_1899.json"), 'r+') as file:
    for json_line in file:
        json_dict = json.loads(json_line)
        acervo = Dict(json_dict)

for i in range(1, len(acervo['_default'])):
    json_list.append(acervo['_default'][str(i)])

df = pd.DataFrame.from_records(json_list).fillna(0)
df = df.replace('\n', '', regex=True)

print('CSV acervo_1556_1899 Criado')
df.to_csv('./Csv/acervo_1556_1899.csv', index=False)

amostra = df.head(300)
print('Amostra do CSV acervo_1556_1899 Criado')
amostra.to_csv('./amostras_csv/acervo_1556_1899.csv', index=False)

json_list = []
with open("%s/%s" % (diretorio, "acervo_1900_1979.json"), 'r+') as file:
    for json_line in file:
        json_dict = json.loads(json_line)
        acervo = Dict(json_dict)

for i in range(1, len(acervo['_default'])):
    json_list.append(acervo['_default'][str(i)])

df = pd.DataFrame.from_records(json_list).fillna(0)
df = df.replace('\n', '', regex=True)

print('CSV acervo_1900_1979 Criado')
df.to_csv('./Csv/acervo_1900_1979.csv', index=False)

amostra = df.head(300)
print('Amostra do CSV acervo_1900_1979 Criado')
amostra.to_csv('./amostras_csv/acervo_1900_1979.csv', index=False)

json_list = []
with open("%s/%s" % (diretorio, "acervo_1980_1989.json"), 'r+') as file:
    for json_line in file:
        json_dict = json.loads(json_line)
        acervo = Dict(json_dict)

for i in range(1, len(acervo['_default'])):
    json_list.append(acervo['_default'][str(i)])

df = pd.DataFrame.from_records(json_list).fillna(0)
df = df.replace('\n', '', regex=True)

print('CSV acervo_1980_1989 Criado')
df.to_csv('./Csv/acervo_1980_1989.csv', index=False)

amostra = df.head(300)
print('Amostra dos CSV acervo_1980_1989 Criado')
amostra.to_csv('./amostras_csv/acervo_1980_1989.csv', index=False)
