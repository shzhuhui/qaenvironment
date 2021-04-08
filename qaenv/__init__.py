import os


__author__ = 'yutiansut'
__version__ = '0.0.2'


mongo_ip = os.getenv('MONGODB', '192.168.0.151')
mongo_port = 27017
mongo_uri = 'mongodb://{}:{}'.format(mongo_ip, mongo_port)


eventmq_ip = os.getenv('QAPUBSUB_IP', '192.168.0.151')
eventmq_port = os.getenv('QAPUBSUB_PORT', 5672)
eventmq_username = os.getenv('QAPUBSUB_USER', 'admin')
eventmq_password = os.getenv('QAPUBSUB_PWD', 'admin')
eventmq_amqp = 'pyamqp://{}:{}@{}:{}//'.format(
    eventmq_username, eventmq_password, eventmq_ip, eventmq_port)



clickhouse_ip =  os.getenv('CLICKHOUSE_IP', '192.168.0.151')

redis_ip = os.getenv('REDIS_IP', '192.168.0.151')