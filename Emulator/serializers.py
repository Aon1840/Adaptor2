from rest_framework import serializers
from Users.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('user_id','username','password','name','surname','tel','email','register_date')
#
#     def create(self, validated_data):
#         #method for create and return new 'User' instance
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         #method for update and return exist 'User' instance
#         instance.username = validated_data.get('username',instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.name = validated_data.get('name', instance.name)
#         instance.surname = validated_data.get('surname', instance.surname)
#         instance.tel = validated_data.get('tel', instance.tel)
#         instance.email = validated_data.get('email', instance.email)
#
#         instance.save()
#         return instance