import unittest
from app.models import Article,News

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('bbc','Trump dies in plane crash','wati','21-04-2019','url','A hot-headed teen slashed a man in the face and then pushed him onto the tracks during a squabble in a Manhattan subway ')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
