import time
from django.core.cache import cache

def attempts(request,tries=4,seconds=60):
	ip = request.META.get('REMOTE_ADDR','')
	if not ip:
		ip = request.META.get('HTTP_X_FORWARDED_FOR','').split(',')[0]
	
	tries-=1
	current_sec = int(time.time())
	record = cache.get(ip)
	if not record or record[0] + seconds < current_sec:
		cache.set(ip,(current_sec,tries))
	else:
		tries = max(-1,record[1]-1)
		cache.set(ip,(record[0], tries))

	return tries
