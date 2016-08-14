from django.db import models
#Define the Thread model. This represents a thread in the message board
class Thread(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='threads') 
    
    class Meta:
        ordering = ('created',)

#Define the message model. This represents a single post in a thread.
class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body_text = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='messages') 
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, verbose_name="thread to which the message belongs", related_name='messages')

    class Meta:
        ordering = ('created',)

