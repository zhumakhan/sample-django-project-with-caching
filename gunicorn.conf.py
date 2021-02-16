from multiprocessing import cpu_count

bind = '0.0.0.0:8000'
worker_class = 'gevent'
workers = cpu_count() * 2 + 1
accesslog = '/logs/gunicorn_access.log'
errorlog = '/logs/gunicorn_error.log'
capture_output = True
