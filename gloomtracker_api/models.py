from django.db import models
from django.contrib.postgres.fields import JSONField


class CharacterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    initial_stats = JSONField()

    def __str__(self):
        return f"{self.name} - {self.description}"


class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class Perk(models.Model):
    uses = models.IntegerField(default=1)
    description = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.uses} - {self.description}"


class Item(models.Model):
    card_number = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    additional_info = JSONField()
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"
