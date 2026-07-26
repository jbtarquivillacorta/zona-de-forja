import sys
import socket

class Cliente_sock:
    host_server:str
    port_server:int
    sock:socket

    def __init__( self, host:str, port:int, tiempoDeEspera:int=10  ):
        self.host_server = host
        self.port_server = port
        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) #ipv4 y protocolo TCP
        self.sock.settimeout( tiempoDeEspera ) #tiempo para esperar respuesta
        
        self.conectar()

    def conectar( self ):
        try:
            self.sock.connect( ( self.host_server, self.port_server ) )
        except Exception as e:
            print( f'Error al conectar: -> {e}' )
            quit()

    def escuchar( self, verRespuesta:bool=True, buff:int= 1020 )->str:#buff es el tamaño de bufer que se espera recibir
        try:
            resp_server = self.sock.recv( buff )
            resp_server = resp_server.decode('utf-8')
        except TimeoutError:
            print( 'no hay respuesta')
            return''

        sys.stdout.write( f'{resp_server}\n' if verRespuesta else '' )
        return resp_server
    
    def enviar( self, msg:str ):
        msg += '\n'
        try:    
            sys.stdout.write( f'enviando:>\t{msg}\n' )
            self.sock.sendall( msg.encode('utf-8') )
        except Exception as e:
            print( 'error al enviar: ', e )
    
    def __del__( self ):
        self.sock.close()
        print( '\tconexion socket cerrada' )