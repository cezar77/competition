from django.db import models


class Competitor(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=100)
    time = models.DateTimeField()
    participants = models.ManyToManyField(
        Competitor,
        related_name='events',
        through='Participant'
    )

    def __str__(self):
        return self.title


class Participant(models.Model):
    ROLES = (
        ('H', 'Home'),
        ('V', 'Visitor'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLES)

    def __str__(self):
        return '{} - {}'.format(self.event, self.get_role_display())
