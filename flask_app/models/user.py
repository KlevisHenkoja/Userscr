from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    db_name = 'userscr'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(user)
        return users
    @classmethod
    def create_user(cls,data):
        query = "insert into users (firstname, lastname, email) values (%(firstname)s,%(lastname)s,%(email)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)