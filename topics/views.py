# topics/views.py
from django.shortcuts import render, get_object_or_404
from .models import Topic

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'topic_list.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    demonstrations = topic.get_demonstrations()
    return render(request, 'topic_detail.html', {'topic': topic, 'demonstrations': demonstrations})
