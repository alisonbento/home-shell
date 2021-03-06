__author__ = 'alisonbento'

import basedao
from src.entities.hsuser import HomeShellUser


class UserDAO(basedao.BaseDAO):

    def __init__(self, connection):
        basedao.BaseDAO.__init__(self, connection, 'hs_users', 'user_id')

    def convert_row_to_object(self, entity_row):
        user = HomeShellUser()

        user.id = entity_row['user_id']
        user.name = entity_row['name']
        user.gender = entity_row['gender']
        user.email = entity_row['email']
        user.locale = entity_row['locale']
        user.created = entity_row['created']
        user.modified = entity_row['modified']

        return user