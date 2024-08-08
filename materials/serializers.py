from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_links


class LessonSerializer(serializers.ModelSerializer):
    video = serializers.URLField(validators=[validate_links])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lessons", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True)

    def get_lesson_count(self, obj):
        return obj.lessons.all().count()

    class Meta:
        model = Course
        fields = ("lesson_count", "lesson", "title", "description")


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
