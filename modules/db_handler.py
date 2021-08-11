from random import randint

from pymongo import MongoClient

client = MongoClient("mongo-temp")
db = client['database']
collection = db['Users']


def insert_user(id: int):
    user = {'_id': id,
            'exp': 0,
            'rolls': {'d20': 0,
                      'd12': 0,
                      'd10': 0,
                      'd8': 0,
                      'd6': 0,
                      'd4': 0
                      },
            'prestige': 0
            }
    collection.insert_one(user)


def check_user(id: int):
    if not bool(collection.find_one({'_id': id})):
        insert_user(id=id)
    return True


def update_user_exp(id: int):
    user_data = collection.find_one({'_id': id})
    if user_data['exp'] >= 50000:
        user_data['exp'] = 0
        user_data['prestige'] += 1
        collection.update_one({'_id': id}, {"$set": {'prestige': user_data['prestige']}})
    user_data['exp'] = user_data['exp'] + randint(15, 50)
    collection.update_one({'_id': id}, {"$set": {'exp': user_data['exp']}})


def update_user_dice(id: int, side: str, rolls: int):
    user_data = fetch_user(id=id)
    if str(side) == 'd20':
        user_data['rolls']['d20'] = user_data['rolls']['d20'] + rolls
        collection.update_one({'_id': id}, {"$set": user_data})
    elif str(side) == 'd12':
        user_data['rolls']['d12'] = user_data['rolls']['d12'] + rolls
        collection.update_one({'_id': id}, {"$set": user_data})
    elif str(side) == 'd10':
        user_data['rolls']['d10'] = user_data['rolls']['d10'] + rolls
        collection.update_one({'_id': id}, {"$set": user_data})
    elif str(side) == 'd8':
        user_data['rolls']['d8'] = user_data['rolls']['d8'] + rolls
        collection.update_one({'_id': id}, {"$set": user_data})
    elif str(side) == 'd6':
        user_data['rolls']['d6'] = user_data['rolls']['d6'] + rolls
        collection.update_one({'_id': id}, {"$set": user_data})
    elif str(side) == 'd4':
        user_data['rolls']['d4'] = user_data['rolls']['d4'] + rolls
        collection.update_one({'_id': id}, {"$set": user_data})


def fetch_user(id: int):
    return collection.find_one({'_id': id})


def drop_user(id: int):
    collection.delete_one({'_id': id})
