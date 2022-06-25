from rest_framework import serializers, status
from rest_framework.views import Response

from .models import *


class CoursesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = "__all__"
        read_only_fields = ["owner"]

    def create(self, validated_data):
        owner = self.context['request'].user
        course = Courses.objects.create(owner=owner, **validated_data)
        course.save()
        return course


class CourseEnrolmentSerializers(serializers.Serializer):
    course = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    class Meta:
        model = CourseEnrolment
        fields = "__all__"

    def get_course(self, obj):
        return str(obj.course.name)

    def get_users(self, obj):
        return str(obj.users.all())
