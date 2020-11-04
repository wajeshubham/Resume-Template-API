from rest_framework import serializers

from .models import *


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        exclude = ('resume',)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('resume',)


class HonorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honours
        exclude = ('resume',)


class ResumeSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True)
    education = EducationSerializer(many=True)
    honours = HonorsSerializer(many=True)

    class Meta:
        model = Resume
        fields = "__all__"
