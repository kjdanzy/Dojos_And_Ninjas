from werkzeug.utils import redirect
from flask_app.config.mysqlconnection import connectToMySQL, log_this

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_this_ninja(cls, data):
        className = "create_this_ninja"
        query = "INSERT INTO NINJAS (FIRST_NAME, LAST_NAME, AGE, DOJO_ID, CREATED_AT) VALUES "
        query += "( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW());"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        log_this(className, data, query, results)
        return results





