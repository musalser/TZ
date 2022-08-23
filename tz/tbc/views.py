from tz.tbc.models import Course
from tz.tbc.serializers import CourseSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
