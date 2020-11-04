from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# READ
class ResumeView(generics.ListAPIView):
    model = Resume
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


# CREATE
class AddEducationView(APIView):

    def post(self, request, **kwargs):
        resume = get_object_or_404(Resume, id=kwargs.get("id"))

        # to make sure that all the fields are being passed from frontend
        if 'college_name' in request.data and \
                'course' in request.data and \
                'start_date' in request.data and \
                'end_date' in request.data and \
                request.data['college_name'] != "" and \
                request.data['course'] != "" and \
                request.data['start_date'] != "" and \
                request.data['end_date'] != "":

            education_details = Education.objects.create(resume=resume,
                                                         college_name=request.data['college_name'],
                                                         course=request.data['course'],
                                                         start_date=request.data['start_date'],
                                                         end_date=request.data['end_date'])

            data = {
                "message": 'Added successfully',
                'status': status.HTTP_200_OK
            }

            return Response(data)
        else:
            data = {
                "message": 'Please add all the fields',
                'status': status.HTTP_400_BAD_REQUEST
            }

            return Response(data)


class AddSkillsView(APIView):

    def post(self, request, **kwargs):
        resume = get_object_or_404(Resume, id=kwargs.get("id"))

        # to make sure that all the fields are being passed from frontend
        if 'skill_name' in request.data and request.data['skill_name'] != "":
            skill = Skills.objects.create(resume=resume,
                                          skill_name=request.data['skill_name'])

            data = {
                "message": 'Added successfully',
                'status': status.HTTP_200_OK
            }

            return Response(data)
        else:
            data = {
                "message": 'Please add all the fields',
                'status': status.HTTP_400_BAD_REQUEST
            }

            return Response(data)


class AddHonoursView(APIView):

    def post(self, request, **kwargs):
        resume = get_object_or_404(Resume, id=kwargs.get("id"))

        # to make sure that all the fields are being passed from frontend
        if 'title' in request.data and \
                'issue_date' in request.data and \
                'description' in request.data and \
                request.data['title'] != "" and \
                request.data['issue_date'] != "" and \
                request.data['description'] != "":

            honor = Honours.objects.create(resume=resume,
                                           title=request.data['title'],
                                           issue_date=request.data['issue_date'],
                                           description=request.data['description'])

            data = {
                "message": 'Added successfully',
                'status': status.HTTP_200_OK
            }
            return Response(data)
        else:
            data = {
                "message": 'Please add all the fields',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data)


# DELETE
class DeleteEducationView(generics.DestroyAPIView):

    def delete(self, request, **kwargs):
        education = get_object_or_404(Education, id=kwargs.get("edu_id"))
        education.delete()

        data = {
            'messege': "deleted successfully",
            'status': status.HTTP_200_OK
        }

        return Response(data)


class DeleteSkillsView(generics.DestroyAPIView):

    def delete(self, request, **kwargs):
        skill = get_object_or_404(Skills, id=kwargs.get("skl_id"))
        skill.delete()

        data = {
            'messege': "deleted successfully",
            'status': status.HTTP_200_OK
        }

        return Response(data)


class DeleteHonourView(generics.DestroyAPIView):

    def delete(self, request, **kwargs):
        honor = get_object_or_404(Honours, id=kwargs.get("hon_id"))
        honor.delete()

        data = {
            'messege': "deleted successfully",
            'status': status.HTTP_200_OK
        }

        return Response(data)


# UPDATE
class UpdateEducationView(generics.UpdateAPIView):

    def put(self, request, *args, **kwargs):
        education = get_object_or_404(Education, id=kwargs.get("edu_id"))

        if 'college_name' in request.data and request.data['college_name'] != "":
            education.college_name = request.data['college_name']

        if 'course' in request.data and request.data['course'] != "":
            education.course = request.data['course']

        if 'start_date' in request.data and request.data['start_date'] != "":
            education.start_date = request.data['start_date']

        if 'end_date' in request.data and request.data['end_date'] != "":
            education.end_date = request.data['end_date']

        education.save()

        data = {
            'messege': "education updated successfully"
        }
        return Response(data)


class UpdateSkillsView(generics.UpdateAPIView):

    def put(self, request, *args, **kwargs):
        skill = get_object_or_404(Skills, id=kwargs.get("skl_id"))

        if 'skill_name' in request.data and request.data['skill_name'] != "":
            skill.skill_name = request.data['skill_name']

        skill.save()

        data = {
            'messege': "skills updated successfully"
        }
        return Response(data)


class UpdateHonourView(generics.UpdateAPIView):

    def put(self, request, *args, **kwargs):
        honor = get_object_or_404(Honours, id=kwargs.get("hon_id"))

        if 'title' in request.data and request.data['title'] != "":
            honor.title = request.data['title']

        if 'issue_date' in request.data and request.data['issue_date'] != "":
            honor.issue_date = request.data['issue_date']

        if 'description' in request.data and request.data['description'] != "":
            honor.description = request.data['description']

        honor.save()

        data = {
            'messege': "honor updated successfully"
        }
        return Response(data)
