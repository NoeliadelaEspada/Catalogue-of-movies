import os

class ServicioPeliculas:

    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf8') as archivo: 
            archivo.write(f'{pelicula.nombre}\n')
        
    def listar_peliculas(self):
        with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
            print('***CATÁLOGO DE PELÍCULAS***')
            print(archivo.read()) 

    def eliminar_archivo_peliculas(self): 
        os.remove(self.nombre_archivo) 
        print(f'Se ha eliminado el archivo {self.nombre_archivo}')

    
        
