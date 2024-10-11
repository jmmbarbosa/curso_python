from pymongo import collection

def get_database():
    from pymongo import MongoClient
    import pymongo
    
    CONNECTION_STRING = "mongodb+srv://j1000tonmjmb:Usrb&n67@cluster0.waacd.mongodb.net/"

    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['sample_airbnb']

get_database()
