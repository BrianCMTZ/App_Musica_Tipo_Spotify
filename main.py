#El caso que elegi es de una aplicacion tipo spotify

class Cancion:
    #Aqui se define el metodo __init__ , aqui relacionamos el self con los atributos seleccionados
    def __init__(self,creditos_cancion, nombre_cancion, duracion_cancion,album,reproducciones:int=0):
        self.creditos_cancion=creditos_cancion
        self.nombre_cancion=nombre_cancion
        self.duracion_cancion=duracion_cancion
        self.album=album
        self.favorito = False
        self.__reproducciones = 0   #<- este es el atributo privado
        self.reproducciones=reproducciones #este es el que pasa por el setter para validarlo 
    
    #Nuevo 5 Nuevo Método getter para consultar las reproducciones de forma segura
    @property
    def reproducciones(self):
        return self.__reproducciones
    #Nuevo 6 En esta parte estamos poniendo un setter para llevar el contador de cuantas reproducciones llevamos
    @reproducciones.setter
    def reproducciones(self, nuevo_total:int):
        if (nuevo_total<0):
            raise ValueError(f"Las reproducciones no pueden ser negativas y mantienen su valor anterior: {self.__reproducciones}")
        self.__reproducciones = nuevo_total

    #1 Aqui estoy poniendo el metodo reproducir album
    def reproducir_cancion(self):
        self.__reproducciones += 1 #Se pone el contador en el def reproducir_cancion
        print(f"Se ha empezado a reproducir la cancion {self.nombre_cancion} del album {self.album}, reproducciones totales:{self.__reproducciones}")

    #2 Aqui defini el metodo minutos escuchados agregando en una nueva variable el conteo de horas escuchdas
    def minutos_escuchados(self,minutos_total):
        minutos_total+=self.duracion_cancion
        print(f"El total de minutos escuchados {minutos_total}")

    #3 Aqui defini el metodo ver informacion de la cancion
    def informacion_cancion(self):
        print(f"Los creditos de la cancion {self.nombre_cancion} son {self.creditos_cancion}")

    #4 Aqui se define si se eligio como favorita la cancion
    def favorita(self,favorito):
        #Esta parte es para modificar el valor de defecto false por true, si asi se quiere
        self.favorito=favorito
        if self.favorito:
            print(f"La canción ahora es favorita")
        else:
            print(f"La cancion no es favorita")

    #7  Subclase con herencia y polimorfismo
class MusicaExclusiva(Cancion):
    def __init__(self, creditos_cancion, nombre_cancion, duracion_cancion, album, plan_suscripcion:str, region:str , reproducciones = 0):
        #Usamos el metodo constructor super() para llamar los atributos de la clase padre 'HERENCIA'
        super().__init__(creditos_cancion, nombre_cancion, duracion_cancion, album, reproducciones)

        #Aqui definimos los atributos propios
        self.plan_suscripcion=plan_suscripcion          #Aqui establecemos el plan de suscripcion por ejemplo :"Premium"
        self.region=region          #Aqui se establece la region si esta disponible por ejemplo algo que este solamente en la region "MX"

    #definimos los metodos de la clase hija
    def descargar_musica(self):
        #En este print llamamos el atributo nombre_cancion de la clase padre y ponemos el atributo propio de la clase hija
        if self.plan_suscripcion.capitalize() == "Premium" or self.plan_suscripcion.capitalize() == "Premium familiar":
            print (f"La descarga de la cancion: '{self.nombre_cancion}' se ha completado, guardada para ser escuchada en: '{self.region}'")
        else:
            print(f"Tu plan '{self.plan_suscripcion}' no permite descargar esta musica en tu región '{self.region}'")

    #Aqui definimos el metodo reproducir_cancion haciendo OVERRRIDE para cambiar el metodo heredado
    def reproducir_cancion(self):
        if self.plan_suscripcion.capitalize() == "Premium" or self.plan_suscripcion.capitalize() == "Premium familiar":
            super().reproducir_cancion()
            print(f"La reproduccion ha comenzado, gracias por usar {self.plan_suscripcion}")
        else:
            print(f"Tu plan {self.plan_suscripcion} no tiene disponible escuchar esta canción") 

#Aqui se crearon los objetos y se hicieron la pruebas correspondientes
#(creditos_cancion, nombre_cancion, duracion_cancion,album)
Cancion_1 = Cancion(
    "Disquera: Parlophone UK, Interpretada por: Coldplay",
    "Sparks",
    3,
    "Parachutes"
)
Cancion_1.reproducir_cancion()
Cancion_1.minutos_escuchados(10)
Cancion_1.informacion_cancion()
Cancion_1.favorita(False)
#Aqui hicimos las funciones de ENCAPSULAMIENTO
print(f"Consulta segura con Getter: {Cancion_1.reproducciones} reproducciones")     #Se ve que el getter funciona de manera correcta
Cancion_1.reproducciones = 25  # Usamos el setter para darle un nuevo valor de forma válida
print(f"Nuevo valor asignado con Setter: {Cancion_1.reproducciones} reproducciones")    #El print del nuevo valor que se le asigno

#En esta parte instanciamos un objeto 'Cancion_2' haciendo que todo se valide correctamente, aplicando el POLIMORFISMO
print("---------------------------")
Cancion_2 = MusicaExclusiva(
    "Disquera: WM Mexico, Interpretada por: Maná",
    "Labios Compartidos",
    5,
    "Amar Es Combatir",
    plan_suscripcion="Premium",
    region="MX"
)

#En esta parte instanciamos un objeto 'Cancion_3' haciendo que sea una prueba de validacion incorrecta, aplicando el POLIMORFISMO
Cancion_2.reproducir_cancion()
Cancion_2.descargar_musica()
Cancion_2.favorita(True)
print("---------------------------")
Cancion_3 = MusicaExclusiva(
    "Disquera: Musart-Balboa, Interpretada por: Joan Sebastian",
    "Eso y Más (Inedita)",
    2,
    "Más alla del sol",
    plan_suscripcion="Gratuito",
    region="USA"
)

Cancion_3.reproducir_cancion()
Cancion_3.descargar_musica()
print("---------------------------")

#Hecho por Brian Cayetano Martínez
