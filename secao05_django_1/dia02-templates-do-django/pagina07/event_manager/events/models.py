# events/models.py
from django.db import models


class Event(models.Model):
    TYPE_CHOICES = (
        ("C", "Conference"),
        ("S", "Seminar"),
        ("W", "Workshop"),
        ("O", "Other"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    is_remote = models.BooleanField(default=False)
    image = models.ImageField(upload_to="events/img", blank=True)

    def __str__(
        self,
    ):  # O método __str__ é sobrescrito para indicar como será a visualização do objeto  # noqa: E501
        return f"{self.title} - {self.date} - {self.location}"  # Título do evento - Data - Local  # noqa: E501


"""
from events.models import Event # importa o modelo Event

Event.objects.all() # retorna todos os eventos do banco. Se você não criou nenhum, o retorno será um QuerySet vazio

Event.objects.create(title='Conferência de Django', description='Evento massa sobre Django', date='2023-09-29 12:00:00-03:00', location='São Paulo', event_type='C', is_remote=False) # cria um novo evento no banco

Event.objects.all() # retorna todos os eventos do banco. Agora o retorno será um QuerySet com um evento a mais

Event.objects.create(title='Django Workshop', description='Workshop que acontece semestralmente sobre Django', date='2024-10-02 15:30:00-03:00', location='Web', event_type='W', is_remote=True) # cria outro evento no banco

Event.objects.filter(is_remote=True) # retorna apenas os eventos do banco que são remotos

Event.objects.filter(event_type='W') # retorna apenas os eventos do banco que são workshops

Event.objects.filter(event_type='C', is_remote=False) # retorna apenas os eventos do banco que são conferências e presenciais, simultaneamente

Event.objects.filter(date__year=2024) # retorna apenas os eventos do banco que acontecem em 2024

Event.objects.filter(date__range=['2023-01-01', '2024-12-31']) # retorna apenas os eventos do banco que acontecem entre 2023 e 2024
"""  # noqa: E501


"""
from events.models import Event # importa o modelo Event

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>]>

evento_1 = Event(title='Django Devs', description='Pessoas fantásticas que usam Django se reunindo em um só lugar', date='2025-07-02 13:30:00-03:00', location='Web', event_type='W', is_remote=True) # instancia um novo evento

evento_1.save() # salva o evento no banco

evento_2 = Event(title='DjangoFest', description='Um festival um pouco menos legal que desenvolver com Django', date='2023-11-22 18:00:00-03:00', location='São Paulo', event_type='C', is_remote=False) # instancia outro evento

evento_2.save() # salva o evento no banco

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>, <Event: Django Devs - 2025-07-02 16:30:00+00:00 - Web>, <Event: DjangoFest - 2023-11-22 21:00:00+00:00 - São Paulo>]>

evento_3 = Event(title='DJ ANGO', description='Conheça a mais nova sensação musical.', date='2027-06-19 20:00:00-03:00', location='São Paulo', event_type='C', is_remote=False) # instancia um evento idêntico ao anterior

evento_3.save() # salva o evento no banco

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>, <Event: Django Devs - 2025-07-02 16:30:00+00:00 - Web>, <Event: DjangoFest - 2023-11-22 21:00:00+00:00 - São Paulo>, <Event: DJ ANGO - 2027-06-19 23:00:00+00:00 - São Paulo>]>

evento_3.delete() # remove o evento do banco

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>, <Event: Django Devs - 2025-07-02 16:30:00+00:00 - Web>, <Event: DjangoFest - 2023-11-22 21:00:00+00:00 - São Paulo>]>
"""  # noqa: E501
