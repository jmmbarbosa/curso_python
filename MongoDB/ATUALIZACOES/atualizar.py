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

#collection_name.update_many({"desconto_maximo":"10%"}, {"$set":{"desconto_maximo":"50%"}})
collection_name.update_one({"nome_item":{"$regex":"Aula"}},{"$set":{"desconto_maximo":"100%"}})
print("Dados atualizados!")

detalhes_itens = collection_name.find()
for item in detalhes_itens:
    print(item)
