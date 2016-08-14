import datetime
import factory
from factory import fuzzy
from . import models
from django.contrib import auth

class User(factory.DjangoModelFactory):

    class Meta:

        model = auth.get_user_model()
        exclude = ('raw_password',)

    first_name = 'Joe'
    last_name = factory.Sequence(lambda n: 'Dirt the {0}'.format(n))
    email = factory.sequence(lambda n: 'account{0}@example.com'.format(n))
    username = 'beest'
    raw_password = 'password123'
    password = factory.PostGenerationMethodCall('set_password', raw_password)
    is_active = True

class Thread(factory.DjangoModelFactory):

    class Meta:
        model = models.Thread

    title = factory.Sequence(lambda n: 'Thread {0}'.format(n))
    owner = factory.SubFactory(User,username="beestThread")
    #owner = factory.StubFactory()
    #owner = factory.RelatedFactory(User)
    created = datetime.date(2016, 8, 13)
    @factory.post_generation
    def messages(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for message in extracted:
                self.messages.add(message)

class Message(factory.DjangoModelFactory):

    class Meta:
        model = models.Message

    title = factory.Sequence(lambda n: 'Message {0}'.format(n))
    owner = factory.SubFactory(User,username="beestMessage")
    #owner = factory.RelatedFactory(User)
    #owner = factory.StubFactory()
    created = datetime.date(2016, 8, 13)
    body_text = fuzzy.FuzzyText(length=400)
    thread = factory.SubFactory(Thread)



