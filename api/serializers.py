from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="pk", read_only=True)
    favoriteFood = serializers.CharField(
        source="favorite_food",
        max_length=100,
    )
    favoriteEmoji = serializers.CharField(
        source="favorite_emoji",
        max_length=20,
    )
    

    class Meta:
        model = Student
        fields = ["_id", "name", "favoriteFood", "favoriteEmoji"]

        