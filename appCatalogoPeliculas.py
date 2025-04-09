from servicioPeliculas import ServicioPeliculas
from pelicula import Pelicula


class AppCatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()
        

    def mostrar_opciones(self):
        while True:
            try:
                print(f''' *** CATÁLOGO DE PELÍCULAS ***
                Opciones:
                1. Agregar película
                2. Lista de películas
                3. Eliminar catálogo de películas
                4. Salir''')
                opcion = int(input('¿Que opción desea realizar?'))
                if opcion == 1:
                   nombre_pelicula = input('Por favor, introduce el título de la película: ')
                   pelicula = Pelicula(nombre_pelicula)
                   self.servicio_peliculas.agregar_pelicula(pelicula)
                   print(f'¡Bien hecho! Has agregado la película {nombre_pelicula} a tu playlist.')
                elif opcion == 2: 
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Gracias, vuelva pronto.')
                    break 
                else:
                    print(f'La opción seleccionada {opcion} no es válida, pruebe otra.')  
            except ValueError:  
                print('Error: Introduce un número válido')
            except Exception as e:
                print(f'Ocurrió un error: {e}')
            
       
if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_opciones()





