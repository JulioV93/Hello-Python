from pymongo import MongoClient

#Base de Datos Local
#db_client = MongoClient().local

#Base de Datos Remota MongoDB Atlas

uri = "mongodb+srv://juliomachadov93:Julio23734267@cluster0.r4fqomi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_client = MongoClient(uri).Cluster0
