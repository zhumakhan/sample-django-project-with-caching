from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class BuyTickerSerializer(serializers.Serializer):
	email = serializers.CharField(label=_('email'))
	stream_id = serializers.IntegerField(label=_("stream_id"))