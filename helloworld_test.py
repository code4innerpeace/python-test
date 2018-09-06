import unittest
import helloworld as HelloWorldClass

class Test(unittest.TestCase):

  def test_greet_user(self):
      helloworld = HelloWorldClass.helloworld()
      print("Checking greeting user functionality\n")
      username = "VAS"
      self.assertEqual(helloworld.greet_user(username),'Hello : VAS')

if __name__ == '__main__':
    unittest.main()
