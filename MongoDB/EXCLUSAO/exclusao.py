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

#collection_name.delete_one({"_id":"SC001"})
collection_name.drop()
print("Dados deletados!")

detalhes_itens = collection_name.find()
for item in detalhes_itens:
    print(item)
