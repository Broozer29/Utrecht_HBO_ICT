import time
import hashlib
import requests
import json
import random

#De eerste URL, om verbinding te makne met de API
firstCall = "http://gateway.marvel.com:80/v1/public/events"


def haalMarvelInfo():
#Maak de eerste call naar de API, en haal een event op. Event in dit geval is een verhaal in een comic.
    events = roepMarvel(firstCall)
    print(events[0]['resourceURI'])

#Selecteer alle namen van de helden die voorkomen in desbetreffend event.
    temp = roepMarvel(events[0]['resourceURI'])
    characters = temp[0]['characters']

#Van de 20 namen die terugkomen, seleteer een willekeurige.
    randomGetal = random.randrange(1,len(characters['items']))
    heldNaam = characters['items'][randomGetal]['name']
    print("Gekozen held: ", heldNaam)

#Roep de URL van de held(in) op.
    heldLink = characters['items'][randomGetal]['resourceURI']
    print("Heldlink: ", heldLink)

#Bepaal in welke comic de held(in) zit.
#Marvel 20 objecten teruggeven, dus kunnen we weer randomGetal gebruiken om een willekeurige comic te selecteren.
    heldComic = roepMarvel(heldLink)
    comicX = heldComic[0]['comics']['items'][randomGetal]['name']
    print("Gekozen comic (hint): ", comicX)

#Bepaal in welk universum de held(in) terugkwam, en leid daarvan af in welke series hij zich bevind.
    heldSerie = roepMarvel(heldLink)
    welkeSerie = heldSerie[0]['series']['items'][0]['resourceURI']
    print("Gekozen serie (URL): ", welkeSerie)

#Selecteer van de serie het event, en kijk naar de personages die er in voorkomen.
    aantalPersonages = roepMarvel(welkeSerie)
#Omdat een comic niet altijd 20 personages heeft, maar ook minder kan hebben, kan hier niet randomGetal gebruikt worden.
#In plaats daarvan wordt het aantal personages uitgerekend, en daar een willekeurige uit gekozen.
    totaalAantalPersonages = len(aantalPersonages[0]['characters']['items'])
    randomPersonageGetal = random.randrange(1,totaalAantalPersonages)
    superheldXNaam = aantalPersonages[0]['characters']['items'][randomPersonageGetal]['name']
    print("Superheld X (hint): ", superheldXNaam)


def roepMarvel(url):
    timestamp = str(time.time())
    private_key = "a458b3fd88726c2ccf88ae1cf3177fb645532df2"
    public_key = "d98db3e2da438da72688319eb2bc9751"
    hash = hashlib.md5((timestamp + private_key + public_key).encode('utf-8'))
    md5digest = str(hash.hexdigest())
    connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
    response = requests.get(connection_url)
    jsontext = json.loads(response.text)  # om de JSON leesbaar te printen... #
    return jsontext['data']['results']


haalMarvelInfo()



##descriptions = [result['description'] for result in results]
##names = [result['name'] for result in results if result['name'] != 'Abyss']


##for result in results:
##    print(result['resourceURI'])

##print(results[0]['title'],results[0]['resourceURI'])


##for description in descriptions:
##    print(description)
##print(timestamp)
##for i in results:
##    if i['name'] == "Aginar":
##        print(i['name'])