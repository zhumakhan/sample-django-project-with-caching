from django.utils.translation import gettext_lazy as _

CACHE_TIMEOUT=86400 #day

KZT = 'KZT'
RUB = 'RUB'
USD = 'USD'

CURRENCIES = (
	(KZT,_(KZT)),
	(RUB,_(RUB)),
	(USD,_(USD)),
)