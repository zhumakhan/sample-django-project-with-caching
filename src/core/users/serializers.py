from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(required=False, write_only=True)
	class Meta:
		 model=User
		 fields = '__all__'
	# def create(self, validated_data):
 #    	return super().create(validated_data)


 #    def update(self, instance, validated_data):
 #        return super().update(instance, validated_data)

 #    def to_representation(self, instance):
 #        representation = super(UserSerializer, self).to_representation(instance)
 #        return representation


class CRMAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs