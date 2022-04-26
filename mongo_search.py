from pymongo import MongoClient

class LearnMongoDBSearc(object):
    """
    MongoDB查询练习
    """

    def __init__(self):
        self.client = MongoClient('mongodb://47.241.35.150:27017/')

    def search_one(self):
        """
        查询一个文档
        :return:
        """
        # user_obj = self.client.test.users.find_one()
        db = self.client.get_database('test')
        users = db.get_collection('users')
        user_obj = users.find_one()
        print(user_obj)

    def search_many(self):
        """
        查询多个文档
        :return:
        """
        db = self.client.get_database('test')
        users = db.get_collection('users')
        stu_list = users.find()
        for item in stu_list:
            print(item)


if __name__ == '__main__':
    obj = LearnMongoDBSearc()
    # obj.search_one()
    obj.search_many()
