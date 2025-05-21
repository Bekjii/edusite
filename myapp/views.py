from django.shortcuts import render, get_object_or_404
from .models import Subject, Grade, Topic, Content


def index(request):
    subjects = Subject.objects.all()
    return render(request, 'myapp/index.html', {'subjects': subjects})


def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    grades = Grade.objects.filter(subject=subject)
    return render(request, 'myapp/subject.html', {'subject': subject, 'grades': grades})


def grade_detail(request, subject_id, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    topics = Topic.objects.filter(grade=grade)
    return render(request, 'myapp/class.html', {'grade': grade, 'topics': topics})


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    contents = Content.objects.filter(topic=topic)
    return render(request, 'myapp/topic.html', {'topic': topic, 'contents': contents})


def content_detail(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, 'myapp/content.html', {'content': content})


def grade_detail(request, subject_id, grade_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    grade = get_object_or_404(Grade, pk=grade_id, subject=subject)
    topics = Topic.objects.filter(grade=grade)
    return render(request, 'myapp/grade_detail.html', {
        'subject': subject,
        'grade': grade,
        'topics': topics
    })


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    contents = Content.objects.filter(topic=topic)
    return render(request, 'myapp/topic.html', {
        'topic': topic,
        'contents': contents
    })
