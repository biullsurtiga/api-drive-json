# Google Drive Api - Json


Coleta de dados em formato json do Google Drive por via Api Google Drive, tratamento via Pandas e exportação em formato csv.

1 - Usando a linguagem Python foi feito o download de Jsons no Google Drive via Api usando os file_id desses arquivos:
```Python
request = drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
```

2 - Depois estruturamos e tratamos os dados Json no DataFrame usando pandas salvas em .csv:
```Python
df = pd.DataFrame.from_records(json_list).fillna(0)
df = df.replace('\n', '', regex=True)

df.to_csv('./Csv/acervo_1556_1899.csv', index=False)
```

3 - Por fim foi extraído uma amostra de 300 linhas dos dados para validação das informações:
```Python
amostra = df.head(300)
amostra.to_csv('./amostras_csv/acervo_1556_1899.csv', index=False)
```
