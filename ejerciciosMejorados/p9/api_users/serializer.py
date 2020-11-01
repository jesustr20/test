from rest_framework import serializers
from .models import Usuario

#CLASE SERIALIZ
class UsarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ['id','first_name','last_name','username','password','email','is_active']

    def create(self, validated_data):
        useradm = Usuario.objects.create(
            username = validated_data['username'],
            email = validated_data["email"],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        useradm.set_password(validated_data["password"])
        useradm.save()
        return useradm

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UsarioSerializer, self).update(instance, validated_data)