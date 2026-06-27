from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Repository, CodeFile
from .serializers import RepositorySerializer, CodeFileSerializer

class RepositoryListCreateView(generics.ListCreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

class RepositoryDetailView(generics.RetrieveAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer


class CodeFileCreateView(generics.CreateAPIView):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileSerializer

class CodeFileSearchView(generics.ListAPIView):
    serializer_class = CodeFileSerializer

    def get_queryset(self):
        queryset = CodeFile.objects.all()
        name = self.request.query_params.get('name')
        language = self.request.query_params.get('language')
        file_type = self.request.query_params.get('type')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if language:
            queryset = queryset.filter(language__icontains=language)
        if file_type:
            queryset = queryset.filter(file_type__icontains=file_type)

        return queryset

class CriticalFilesView(APIView):

    def get(self, request):
        critical_files = []

        for f in CodeFile.objects.all():
            reasons = []

            if f.size > 1000000:  # plus de 1 Mo
                reasons.append("Taille élevée")
            if f.file_type == 'config':
                reasons.append("Fichier de configuration")
            if f.file_type == 'security':
                reasons.append("Fichier de sécurité")
            if not f.description:
                reasons.append("Absence de description")

            if reasons:
                data = CodeFileSerializer(f).data
                data['critical_reasons'] = reasons
                critical_files.append(data)

        return Response(critical_files)