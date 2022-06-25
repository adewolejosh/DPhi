
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from .models import Courses, CourseEnrolment
from .serializers import CoursesSerializers, CourseEnrolmentSerializers
from .permissions import EducatorPerms, NonEducatorPerms, IsOwner


class CreateCourses(APIView):
    permission_classes = [IsAuthenticated, EducatorPerms]

    def post(self, request):
        serializer = CoursesSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListAllCourses(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Courses.objects.all()
        serializer = CoursesSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OneCourse(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            queryset = Courses.objects.get(pk=id)
            serializer = CoursesSerializers(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Courses.DoesNotExist:
            return Response({"message": "Not Exist"}, status=status.HTTP_404_NOT_FOUND)


class CourseEnrol(APIView):
    permission_classes = [IsAuthenticated, NonEducatorPerms]

    def post(self, request, id):
        try:
            user = request.user
            course = get_object_or_404(Courses, pk=id)
            enrolled = CourseEnrolment.objects.get(course=course)

            if enrolled:
                if user in enrolled.users.all():
                    return Response({"message": "user already enrolled"}, status=status.HTTP_208_ALREADY_REPORTED)

                else:
                    enrolled.users.add(user)
                    enrolled.save()

            else:
                enrol = CourseEnrolment()
                enrol.course = course
                enrol.save()
                enrol.users.add(user)
                enrol.save()

            return Response({"message": f"{user} enrolled in {course.name}!"}, status=status.HTTP_201_CREATED)

        except ValueError:
            return Response({"message": ValueError}, status=status.HTTP_404_NOT_FOUND)


class ViewEnrols(APIView):
    permission_classes = [IsAuthenticated, IsOwner, EducatorPerms]

    def get(self, request, id):
        queryset = CourseEnrolment.objects.get(course=id)
        serializer = CourseEnrolmentSerializers(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
