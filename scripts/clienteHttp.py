import http.client

class Cliente_http:
    client: http.client
    dominio:str
    puerto:int
    data:http.client.HTTPResponse
    docHtml:str

    def __init__( self, dominio, port:int= 80 ):
        self.dominio = dominio
        self.puerto = port
        self.usarProtocolo( 'http' )    

    def usarProtocolo( self, protocolo:str ): #solo crea conexion no hace ninguna peticion
        if protocolo.lower() == 'http':
            self.client = http.client.HTTPConnection( self.dominio, self.puerto )
        elif protocolo.lower() == 'https':
            self.client = http.client.HTTPSConnection( self.dominio, self.puerto )
        else:
            return
    
    def obtenerHtml( self, respuesta:http.client ):
        self.data = respuesta.getresponse() #self.client.getresponse() solo se puede usar una vez por peticion por eso lo guardamos en self.data

    def peticion( self, metodo:str, path:str='/', header:dict=None ):
        self.client.request( metodo.upper(), path, headers=header or {} )
        self.obtenerHtml( self.client )
        
    def get( self, path:str='/',header:dict=None ):
        self.client.request( 'GET', path, headers=header or {} )
        self.obtenerHtml( self.client )
    
    def post( self, path:str='/',header:dict=None ):
        self.client.request( 'POST', path, headers=header or {} )
        self.obtenerHtml( self.client )
 
    def respuesta( self, verRespuesta:bool=True, codificacion:str='latin-1' ) -> str: #latin-1 es la ISO-8859-1 define la codificacion del alfabeto espaniol
        respuesta = self.data.read().decode( codificacion ) 

        if respuesta == '':
            respuesta = self.docHtml
        else:
            self.docHtml = respuesta

        print( respuesta if verRespuesta else '' )
        return respuesta

    def data_headers( self, v:bool = True, header:str='' ) -> str | dict:#el header especifica el encabezado que queremos extraer
        if header == '':
            print( dict(self.data.getheaders()) if v else '' ) #todos los encabezados
            return dict(self.data.getheaders())

        return self.data.getheader( header ) if header in dict(self.data.getheaders()) else '' 

    def __del__( self ):
        self.client.close()