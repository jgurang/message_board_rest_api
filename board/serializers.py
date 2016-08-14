from rest_framework import serializers
from board.models import Thread, Message
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    threads = serializers.HyperlinkedRelatedField(many=True, view_name='thread-detail',queryset=Thread.objects.all(), required=False)
    messages = serializers.HyperlinkedRelatedField(many=True, view_name='message-detail',queryset=Message.objects.all(), required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'threads', 'messages')
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    thread = serializers.HyperlinkedRelatedField(many=False, view_name='thread-detail',queryset=Thread.objects.all(),required=False)
    class Meta:
        model = Message
        fields = ('id', 'title', 'body_text', 'owner', 'thread')
class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    messages = serializers.HyperlinkedRelatedField(many=True, view_name='message-detail',queryset=Message.objects.all())
    class Meta:
        model = Thread
        fields = ('id', 'title', 'owner', 'messages')
