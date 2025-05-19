from rest_framework import serializers
from .models import Registration  # Ensure the model name matches your actual model

class RegistrationSerializer(serializers.ModelSerializer):  # Fixed the class name
    class Meta:
        model = Registration  # Ensure this matches models.py
        fields = '__all__'

    def validate(self, data):  # Correct placement of validation function
        if data.get('password') != data.get('confirm_password'):  # Fixed typo in field name
            raise serializers.ValidationError("Passwords do not match.")
        return data