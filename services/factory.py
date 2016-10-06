# -*- coding: utf-8 -*-

import factory
import faker
import datetime

from django.conf import settings

from .models import Service, Category
from semillas_backend.users.models import User

faker = faker.Factory.create()
categories=[
	"Atención a las personas",
	"Tareas domésticas",
	"Cuidado del cuerpo y la salud",
	"Construcción, reparaciones, jardinería",
	"Transporte y distribución",
	"Ocio y deportes",
	"Cultura y artes",
	"Música y baile",
	"Educación y formación",
	"Medio ambiente",
	"Animación, artesanía, hobbies",
	"Asesoramiento y orientación",
	"Idiomas",
	"Informática",
	"Gestión y administración"
]

class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=3))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=20))
    author = factory.Iterator(User.objects.all())
    category = factory.Iterator(Category.objects.all())
    date = factory.Sequence(lambda n: datetime.datetime.now() + datetime.timedelta(days=n))
    seeds_price = factory.Faker('pyint')
    

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

	order=count(Category.objects.all())
    name = categories[order]
    if not name:
    	name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=3))
