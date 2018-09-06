class helloworld:
  def greet_user(self, username):
    return "Hello : {username}".format(username=username)

if __name__ == '__main__':
  helloworld = helloworld()
  print(helloworld.greet_user("VAS"))
