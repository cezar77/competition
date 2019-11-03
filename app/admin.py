from django.contrib import admin

from .models import Competitor, Event, Participant


class ParticipantInline(admin.StackedInline):
    model = Participant
    max_num = 2


class CompetitorAdmin(admin.ModelAdmin):
    fields = ('name', 'city',)


class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'venue', 'time',)
    inlines = [ParticipantInline]


admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Event, EventAdmin)
