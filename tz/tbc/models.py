from django.db import models


class Course(models.Model):
    id = models.PositiveIntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=253, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner_id = models.PositiveIntegerField(null=True)
    owner_name = models.CharField(max_length=253, null=True)
    duration = models.PositiveIntegerField(null=True)
    video_url = models.TextField(null=True)
    demo = models.BooleanField(null=True)
