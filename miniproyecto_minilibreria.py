class Book:
    #metodo: una funcion asociada a un objeto
    def __init__(self,tittle,autor,price,stock,oid):
        self._title =tittle
        self._autor =autor    
        self._price =price
        self._stock = stock   
        self._oid = oid
    def getInfo(self):
        return f""" \n Titulo {self._title}\n Autor:{self._autor}\n Precio:${self._price}\n Existencias:{self._stock}\n ID:{self._oid}"""
    #publico == accesible para todos
    # protegido "_"== solo se deberia accederse desde la propia clase y sus subclases
    #private "__" = solo es accesible por su propia clase
    #Getters / Setters
    #get -> obtener(lectura)
    #setters -> setear/establecer(escritura)

    def get_title (self):
        return self._title
    def set_title(self,new_title):
        self._title =new_title
    def get_price(self):
        return self._price
    def set_price(self,new_price):
        if new_price > 0:
            self._price =new_price
        else:
            print ("El precio no puede ser 0 o menor")    
class Comic(Book):
    def __init__(self,tittle,autor,price,stock,oid,illustrators,vol):
        super ().__init__(tittle,autor,price,stock,oid)
        self._illustrators = illustrators
        self._vol = vol
    def getInfo(self):
        info = super().getInfo()
        return info + f"""\n Ilustradores: {self._illustrators}\n Vol:{self._vol}\n"""
        # return super().getInfo()    
        



#instanciar
book1= Book('MI LUCHA','ADOLF HITLER',1.500,100,1)
book2= Book('Veinte poemas de amor y una canción desesperada','Pablo Neruda',500.0,50,2)
#print(book1.getInfo())
#print (book2.getInfo() )
#print(book1.get_title())
#book1.set_title('MY FIGHT')
#book1.set_price(0)

#print(book1.getInfo())
comic1 = Comic('The amazing Spider-Man','David Michelinie, Todd McFarlane',250.0,10,1,'No se sabe',1)
print ( comic1.getInfo() )