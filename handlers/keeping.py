from .parsing import parser
import json
import os

class keeper:

    filename = os.path.abspath(os.curdir) + "/handlers/cache/{}.json"

    @staticmethod
    def upload(*args):
        with open(keeper.filename.format(*args), "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    @staticmethod
    def save(*args, **kwargs):
        with open(keeper.filename.format(*args), "w", encoding="utf-8") as file:
            json.dump(parser.update(**kwargs), file, indent=4)

    @staticmethod
    def chek_new(*args, **kwargs):

        old_data = keeper.upload(*args)
        new_data = parser.update(**kwargs)

        new_id = new_data.keys()
        old_id = old_data.keys()
        recent_id = list(set(new_id)-set(old_id))
        keeper.save(*args, **kwargs)

        return any(recent_id), recent_id






