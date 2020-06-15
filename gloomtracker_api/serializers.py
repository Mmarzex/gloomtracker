from rest_framework import serializers
from .models import CharacterClass, Character, Item, Perk


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'additional_info')


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = ('id', 'description', 'uses')


class CharacterClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = CharacterClass
        fields = ('id', 'name', 'description', 'initial_stats')


class CharacterSerializer(serializers.ModelSerializer):
    perks = PerkSerializer(source='perk_set', many=True)
    items = ItemSerializer(source='item_set', many=True)

    class Meta:
        model = Character
        depth = 1
        fields = ('id', 'name', 'level', 'xp', 'character_class', 'perks', 'items')
