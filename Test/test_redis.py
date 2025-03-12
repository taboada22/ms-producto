import os, unittest
from redis import Redis
from app import create_app, db


class RedisTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        
        self.app_context.push()
        

    def tearDown(self):
        self.app_context.pop()

    # test connection to Redis
    def test_redis_connection(self):
        redis = Redis(
            host=self.app.config['CACHE_REDIS_HOST'],
            port=self.app.config['CACHE_REDIS_PORT']
        )
        self.assertTrue(redis.ping())
    
if __name__ == '__main__':
    unittest.main()
