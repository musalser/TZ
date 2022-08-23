from tz.tbc.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False, max_length=253)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    owner_id = serializers.IntegerField(required=False)
    owner_name = serializers.CharField(required=False, max_length=253)
    duration = serializers.IntegerField(required=False, allow_null=True)
    video_url = serializers.CharField(required=False, allow_blank=True)
    demo = serializers.BooleanField(required=False)

    class Meta:
        model = Course
        fields = ('id', 'name', 'created_at', 'updated_at', 'owner_id', 'owner_name', 'duration', 'video_url', 'demo')

