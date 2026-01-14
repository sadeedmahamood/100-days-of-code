# class User:
#   pass

# user_1 = User()
# user_1.id = "1"
# user_1.username = "saah"

# print(user_1.id)


class User:
  def __init__(self, user_id, user_name):
    print("User created successfully")
    self.id = user_id
    self.user_name = user_name

user_1 = User(11, "saah")
print(user_1.user_name)


    

