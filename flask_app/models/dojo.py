import flask_app
from flask_app.config.mysqlconnection import connectToMySQL, log_this
from flask_app.models.ninja import Ninja
from flask_app.models import ninja



class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []    
        
    @classmethod
    def get_all_dojos(cls):
        className = "get_all_dojos"
        query = "SELECT * FROM DOJOS;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        log_this(className, "", query, results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_selected_dojo(cls, data):
        className = "get_selected_dojo"
        query = "SELECT * FROM DOJOS LEFT JOIN NINJAS ON NINJAS.DOJO_ID = DOJOS.ID WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        log_this(className, data, query, results)
        
        dojo = cls(results[0])

        for db_result in results:
            ninja_data = {
                "id": db_result["id"],
                "first_name": db_result["first_name"],
                "last_name": db_result["last_name"],
                "age": db_result["age"],
                "dojo_id": db_result["dojo_id"],
                "created_at": db_result["created_at"],
                "updated_at": db_result["updated_at"]
            }

            dojo.ninjas.append(ninja.Ninja(ninja_data))

        log_this(className, data, query, results)
        return dojo

    @classmethod
    def create_a_dojo(cls, data):
        className = "create_a_dojo"
        query = "INSERT INTO DOJOS (NAME, CREATED_AT) VALUES ( %(name)s, NOW());"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        log_this(className, data, query, results)
        return results




