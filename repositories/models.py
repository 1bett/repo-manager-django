from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CodeFile(models.Model):

    TYPE_CHOICES = [
        ('source', 'Source'),
        ('config', 'Configuration'),
        ('security', 'Security'),
        ('other', 'Other'),
    ]

    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=500)
    file_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='other')
    language = models.CharField(max_length=100, blank=True)
    size = models.PositiveIntegerField(help_text="Taille en octets")
    description = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name