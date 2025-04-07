import os

class ServicioPeliculas:

    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf8') as archivo: # UTF8 se utiliza para que acepte cualquier tipo de caracter
            archivo.write(f'{pelicula.nombre}\n')
        
    def listar_peliculas(self):
        with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
            print('***CATÁLOGO DE PELÍCULAS***')
            print(archivo.read()) # Podríamos hacer una iteración, pero para simplificarlo usaremos el método read, el cual lee toda la información de nuestro archivo y la imprime en el print. 

    def eliminar_archivo_peliculas(self): #Con este método eliminamos el archivo como tal
        os.remove(self.nombre_archivo) #Utilizamos este método que elimina el archivo del sistema operativo, el parámetro es el nombre del archivo que queremos eliminar.
        print(f'Se ha eliminado el archivo {self.nombre_archivo}')

    
        