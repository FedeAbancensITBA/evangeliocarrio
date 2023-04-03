import tweepy
import requests
from bs4 import BeautifulSoup
import tweepy
import textwrap
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

api_key = "LLNyI1BWr4MYd6dE59eLyIwwl"
api_secret = "eF2l88W9sMsIgRjsdhGYPMr696oIwF3cOuFllLHCdJ5rSGdUWV"
access_token = "1642320850039734273-fRd8bOSLddzKWHyUnfjWTnaxkDp0yC"
access_token_secret = "oQTole31AbguMOzfds7F2N7XqMzN1kIPzd2arK0qNRGka"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAN7QmQEAAAAAKTZPFTxf3pJv1geAT0XNM0b2ijw%3DWTPmJghXkLhG3iumewu3oVDlXdXB0NcFK1fI9RNwfHVEu7ZhIy"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Obtén el día de la semana actual
today = datetime.datetime.today()
weekday = today.weekday()
print(weekday)

# Si es domingo (0), haz algo
if weekday == 6:
    url = "https://www.dominicos.org/predicacion/evangelio-del-dia/hoy/lecturas/"
# Si es cualquier otro día, haz algo diferente
else:
    url = "https://www.dominicos.org/predicacion/evangelio-del-dia/hoy/#"

# Realizar una petición GET a la página web
response = requests.get(url)

# Crear un objeto de BeautifulSoup con el contenido HTML de la página web
soup = BeautifulSoup(response.content, "html.parser")

evangelio_del_dia = soup.find("h2", text="Evangelio del día").find_next_sibling()
autor = evangelio_del_dia.text + " - "

evangelio2 = evangelio_del_dia.find_next_sibling()
evangelio3 = evangelio2.find_next_sibling().text

# obtener el nombre del día de la semana y formatear la fecha
dia_semana = today.strftime("%A")
fecha_formateada = today.strftime(f"{dia_semana}, %d de %B")


inicial = "Lean el Evangelio de hoy 🙏 "+ fecha_formateada +"\n\nDios salva al mundo ❤\n\n @elisacarrio\n\n" + url
frases = textwrap.wrap(autor + evangelio3, width=280)
frases.insert(0, inicial)

if (len(frases)>20):    
    tw1 = client.create_tweet(text = frases[0])
    var = tw1.data['id']
    print(frases[0])
    for a in range(1,20):
        tw2 = client.create_tweet(text = frases[a], in_reply_to_tweet_id = var)
        var = tw2.data['id']
        #print(frases[a])
        print("publicados: ", a+1, "de ", len(frases))
    final = "Sigue en " +  url
    print(final)
    tw2 = client.create_tweet(text = frases[a], in_reply_to_tweet_id = var)
    var = tw2.data['id']

else:
    tw1 = client.create_tweet(text = frases[0])
    var = tw1.data['id']
    print("publicados: 1 de ", len(frases))
    for a in range(1, len(frases)):
        tw2 = client.create_tweet(text = frases[a], in_reply_to_tweet_id = var)
        var = tw2.data['id']
        print("publicados: ", a+1, "de ", len(frases))
        #print(frases[a])

