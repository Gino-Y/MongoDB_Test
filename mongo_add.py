from datetime import datetime
from pymongo import MongoClient
from datetime import datetime


class LernMongoDB(object):

    def __init__(self):
        self.client = MongoClient('mongodb://47.241.35.150:27017/')

    def add_one(self):
        '''
        新增一个文档
        :return:
        '''
        doc = {
            'username': '丽丽2',
            'password': '123456',
            'reg_date': datetime.now(),
            'company': {
                'name': '**科技公司',
                'tel': '0000-0000'
            }
        }
        db = self.client.test
        result = db.users.insert_one(doc)
        print(result.inserted_id)

    def add_many(self):
        """
        新增多个文档
        :return:
        """
        doc1 = {
            'username': '李磊',
            'password': '123456',
            'reg_date': datetime.now(),
            'company': {
                'name': '**科技公司',
                'tel': '0000-0000'
            }
        }
        doc2 = {
            'username': '韩梅梅',
            'password': '123456',
            'reg_date': datetime.now(),
            'company': {
                'name': '**科技公司',
                'tel': '0000-0000'
            }
        }
        doclist = [doc1, doc2]
        result = self.client.test.users.insert_many(doclist)
        print(result.inserted_ids)
        print('成功的插入了 {a} 条文档'.format(a=len(result.inserted_ids)))


if __name__ == '__main__':
    obj = LernMongoDB()
    # obj.add_one()
    for i in range(100):
        obj.add_many()
