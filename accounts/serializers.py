from rest_framework import serializers
from django.contrib.auth.models import User

from .constants import USER_CATEGORY
from .models import UserExtension


class CreateUserSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=USER_CATEGORY, default='NE')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'category']

    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            if existing.is_active:
                raise serializers.ValidationError(
                    "Someone with that Email Address has already registered."
                )
        return email

    def create(self, validated_data):
        categ = validated_data.pop('category')

        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        ext = UserExtension.objects.create(user=user, category=categ)
        ext.save()
        return user
