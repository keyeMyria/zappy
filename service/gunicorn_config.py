import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
worker_connections = 2000

accesslog = 'gaccess.log'
errorlog = 'gerror.log'
loglevel = 'warning'
