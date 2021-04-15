from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import io
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    drive_service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = drive_service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

    file_ids = ['1bV0vXsLmHB9AWLBe9b5hMyjdH_0iSlUU', '12yWNF6S8NdG_9SyFaf-2MGKgMUoz2-vg', '1n1e11SFz8XSu'
                                                                                          '-SnyEYgO4AKrmr1HcdeW']
    file_names = ['acervo_1980_1989.json', 'acervo_1900_1979.json', 'acervo_1556_1899.json']

    for file_id, file_name in zip(file_ids, file_names):

        request = drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)

        done = False

        while not done:
            status, done = downloader.next_chunk()
            print("Download progress {0}".format(status.progress() * 100))

        fh.seek(0)
        with io.open(os.path.join('./Jsons', file_name), 'wb') as f:
            f.write(fh.read())
            f.close()


if __name__ == '__main__':
    main()
