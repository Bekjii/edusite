from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Grade(models.Model):
    number = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Topic(models.Model):
    title = models.CharField(max_length=200)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

class Content(models.Model):
    CONTENT_TYPES = [
        ('presentation', 'Презентация'),
        ('game', 'Игра'),
        ('template', 'Шаблон'),
        ('quiz', 'Куиз'),
        ('test', 'Тест'),
        ('video', 'Видео'),
    ]
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
