from rest_framework import serializers
from .models import Repository, CodeFile


class CodeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeFile
        fields = '__all__'


class RepositorySerializer(serializers.ModelSerializer):
    files = CodeFileSerializer(many=True, read_only=True)

    class Meta:
        model = Repository
        fields = '__all__'