import unittest
from app.models import Post, User, Comment

class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_user = User(first_name='Lorraine',last_name='simotwo',username='raine',pass_secure='1234',email='simotwo@gmail.com')
        self.new_post = Post(post_title='unittests',post_content='learning on python flask unittest models',user_id=self.new_user.id)
        self.new_comment = Comment(comment='great concepts',user_id=self.new_user.id,post_id=self.new_post.id)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))