import requests 





class Request:
    def __init__(self):
        self.url = "https://andreshoward.com/pharmacies"
        pass
    
    def get(self):
        solicitud = requests.get(self.url)
        lista = solicitud.json()
        return lista
    
class Summary:
    def __init__(self, lista):
        self.__data__ = lista
        self.__frequencies__ = {}
    
    def call(self):
        for i in self.__data__:
            nombre_farmacia = i['local_nombre']
            self.__frequencies__[nombre_farmacia]=0
        return self.__frequencies__
    
    
    
    def __process_element__(self, diccionario):
        nombre_farmacia = diccionario['local_nombre']
        if nombre_farmacia in self.__frequencies__:
            self.__frequencies__[nombre_farmacia]+=1
        
    
    
    def __build_summary__(self):
        for i in self.__data__:
            self.__process_element__(i)
            
            
            

        
        
        
    
    
    












class Filter:
    def __init__(self, dic):
        self.__data__ = dic
    def apply(self,cadena):
        if cadena in self.__data__:
            return self.__data__[cadena]
        
        
        
        


class Main(Request, Summary, Filter):
    def __init__(self):
        self.__url__ = "https://andreshoward.com/pharmacies"
    
    def main(self):
        request_obj = Request()
        req_get = request_obj.get()
        suma_obj = Summary(req_get)
        suma_obj.call()
        suma_obj.__build_summary__()
        freq_list = suma_obj.__frequencies__
        filt_obj = Filter(freq_list)
        farmacia = input("Ingrese nombre de la farmacia: ")
        c = filt_obj.apply(farmacia)
        return c
    
    

        
        
main_obj = Main()


main_obj.main()

        
        

    



        
        
        