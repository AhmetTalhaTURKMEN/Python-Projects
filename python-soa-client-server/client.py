import xmlrpc.client

# Sunucuya bağlanın
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    # Hizmeti çağırın
    result = proxy.add(4, 5)
    print("4 + 5 = %d" % result)