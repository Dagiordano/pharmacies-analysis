import requests 





class Request:
    def __init__(self):
        self.url = "https://andreshoward.com/pharmacies"
        pass
    
    def get(self):
        solicitud = requests.get(self.url)
        lista = solicitud.json()
        return lista
    
class Sumary:
    def __init__(self, lista):
        self.__data__ = lista
        self.__frequencies__ = {}
    
    def call(self):
        for i in self.__data__:
            nombre_farmacia = i['local_nombre']
            self.__frequencies__[nombre_farmacia]=0
        return self.__frequencies__
    
    



r = requests.get("https://andreshoward.com/pharmacies")

lista = r.json()

chica =lista[0]


suma= Sumary(lista)

suma.call()


        
        
    

        
        



        
        

    



        
        
        