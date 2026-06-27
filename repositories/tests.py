from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Repository, CodeFile


class RepositoryTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.repo = Repository.objects.create(
            name="Mon Repo",
            description="Un repo de test"
        )

    def test_lister_repositories(self):
        response = self.client.get('/api/repositories/')
        self.assertEqual(response.status_code, 200)

    def test_creer_repository(self):
        data = {'name': 'Nouveau Repo', 'description': 'Description'}
        response = self.client.post('/api/repositories/', data)
        self.assertEqual(response.status_code, 201)

    def test_detail_repository(self):
        response = self.client.get(f'/api/repositories/{self.repo.id}/')
        self.assertEqual(response.status_code, 200)


class CodeFileTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.repo = Repository.objects.create(
            name="Repo Test",
            description="Test"
        )
        self.file = CodeFile.objects.create(
            repository=self.repo,
            name="main.py",
            path="/src/main.py",
            file_type="source",
            language="Python",
            size=500,
            description=""
        )

    def test_creer_fichier(self):
        data = {
            'repository': self.repo.id,
            'name': 'config.yml',
            'path': '/config.yml',
            'file_type': 'config',
            'language': 'YAML',
            'size': 200,
            'description': ''
        }
        response = self.client.post('/api/files/', data)
        self.assertEqual(response.status_code, 201)

    def test_recherche_par_langage(self):
        response = self.client.get('/api/files/search/?language=Python')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_fichiers_critiques(self):
        response = self.client.get('/api/files/critical/')
        self.assertEqual(response.status_code, 200)
        # le fichier sans description doit être critique
        self.assertEqual(len(response.data), 1)
        self.assertIn('Absence de description', response.data[0]['critical_reasons'])