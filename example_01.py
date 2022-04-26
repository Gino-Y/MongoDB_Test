from pymongo import MongoClient

# client = MongoClient()

# client = MongoClient('localhost', 27017)

client = MongoClient('mongodb://47.241.35.150:27017/')
print(client)

db = client.test
# db = client['tamp']
# db = client.get_database(name='test')

# db_list = client.list_databases()
# db_list = client.list_database_names()
# for item in db_list:
#     print(item)

# db_test = client.get_database(name='test')
# for item in db_test.list_collection_names():
#     print(item)

# data = db_test.one.find_one()
# data = client.test.one.find_one()
# data = client.test.get_collection('one').find_one()
# print(data)