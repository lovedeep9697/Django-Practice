import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'Django-Practice.settings')

import django
django.setup()


import random
from faker import Faker
from AppTwo.models import Topic, Webpage




fakegen = Faker()
topics = ['search' , 'movies' , 'astronomy' , 'cs']

def add_topic():
	t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
	t.save()
	return t

def populate(N=7):

	for entry in range(N):

		top = add_topic()

		fake_name = fakegen.company()
		fake_url  = fakegen.url()

		webpage = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]


if __name__ == '__main__':

	print('populating DB')
	populate(10)
	print('POPULATED SUCCESSFULLY')

