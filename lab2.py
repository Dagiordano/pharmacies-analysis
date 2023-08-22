import requests 
r = requests.get("https://andreshoward.com/pharmacies")

diccionarios= r.json()

a = diccionarios




class Request():
    self.url = "https://andreshoward.com/pharmacies"
    def __init__(self):
        pass
    
    def get(self):
        solicitud = requests.get(url)
        lista = solicitud.json()
        return lista
    
class Sumary:
    __data__ = ()
    __frequencies = {}
    
    
        
        
        