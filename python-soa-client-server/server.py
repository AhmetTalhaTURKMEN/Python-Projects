from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Hesaplamayı yapacak fonksiyon
def add(a, b):
    return a + b

# Sunucuyu oluşturun
with SimpleXMLRPCServer(('localhost', 8000)) as server:
    # Yöntemleri sunucuya kaydedin
    server.register_function(add, 'add')
    
    # Sunucuyu başlatın
    server.serve_forever()