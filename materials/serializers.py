from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer(source="lessons", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True)

    def get_lesson_count(self, obj):
        return obj.lessons.all().count()

    class Meta:
        model = Course
        fields = ("lesson_count", "lesson", "title", "description")
