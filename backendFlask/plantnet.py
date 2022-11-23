import requests
import json

API_KEY = "2b10vOWpgAoY62YLF1X5UiDzu"  # API_KEY dal mio account plantNet
PROJECT = "weurope"  #identifica la zona di interesse in cui fare la ricerca
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"  #url a cui fare la richiesta
data = {
    'organs': ['leaf', 'leaf', 'leaf', 'leaf']
}  #deve esere della stessa lunghezza della lista di immagini


class PlantNet:

    def __init__(self, photos):
        self.photos = photos  #foto è una lista di max 5 immagini da inviare alla api


#metodo deve leggere la lista di foto in entrata, e per ogni elemento estrarre il binario (con 'rb') salvato in img_data
#poi deve riempire la lista 'file' con il path dell'immagine e relativo bianrio
#il limite delle 5 foto lo mettiamo qui o nel form html? o entrambi?

    def readImg(photos):
        files = []
        if len(photos) <= 5:
            for photo in photos:
                image_data = open(photo, 'rb')
                files.append(('images', (photo, image_data)))
        return files

    def sendImg(files):
        req = requests.Request('POST',
                               url=api_endpoint,
                               files=files,
                               data=data)
        prepared = req.prepare()
        s = requests.Session()
        response = s.send(prepared)
        json_result = json.loads(response.text)

        return json_result