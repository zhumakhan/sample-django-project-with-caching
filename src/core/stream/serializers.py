
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Stream


class StreamSerializer(serializers.ModelSerializer):
	class Meta:
		 model=Stream
		 fields = '__all__'
	# def create(self, validated_data):
 #    	return super().create(validated_data)


 #    def update(self, instance, validated_data):
 #        return super().update(instance, validated_data)

 #    def to_representation(self, instance):
 #        representation = super(UserSerializer, self).to_representation(instance)
 #        return representation


class CheckCodeStreamSerializer(serializers.Serializer):
    code = serializers.CharField(label=_("code"))
    stream_id = serializers.IntegerField(label=_("stream_id"))

class CheckCodeSerializer(serializers.Serializer):
    code = serializers.CharField(label=_("code"))

class CheckTokenSerializer(serializers.Serializer):
    token = serializers.CharField(label=_("token"))

# class GetNewCodeSerializer(serializers.Serializer):
# 	email = serializers.CharField(label=_('email'))
# 	stream_id = serializers.IntegerField(label=_("stream_id"))