from pymongo import collection

def get_database():
    from pymongo import MongoClient
    import pymongo
    
    CONNECTION_STRING = "mongodb+srv://j1000tonmjmb:Usrbin67@cluster0.waacd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0py"

    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']

dbname = get_database()
collection_name = dbname["itens_soulcode"]

#detalhes_itens = collection_name.distinct("categoria")
#detalhes_itens = collection_name.find({"categoria":"Físico"}).limit(2)
detalhes_itens = collection_name.find({}, {"nome_item", "desconto_maximo"}).skip(2)
for item in detalhes_itens:
    print(item)
