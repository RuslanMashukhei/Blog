from .models import Admin,User
from rest_framework import serializers


class AdminSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=10, write_only=True)
    password_confirm = serializers.CharField(max_length=10, write_only=True)
    email = serializers.CharField(max_length=30, write_only=True,allow_blank=True)

    class Meta:
        model = Admin
        fields = '__all__'
        read_only_fields = ['user',]

    def validate(self,data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Пароли должны совпадать!')
        return data

    def create(self, validated_data):
        try:
            new_user = User(username=validated_data['username'],
                            email=validated_data['email'])
            new_user.set_password(validated_data['password'])
            new_user.save()
        except Exception as e:
            return serializers.ValidationError(f'Не удается создать пользователя ю {e}')
        else:
            author = Admin.objects.create(user=new_user)
            return author