from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    # read urls
    path("",ResumeView.as_view(),name="resume"),

    # create urls
    path("<int:id>/add_education/",AddEducationView.as_view(),name="add_education"),
    path("<int:id>/add_skill/",AddSkillsView.as_view(),name="add_skill"),
    path("<int:id>/add_honour/", AddHonoursView.as_view(), name="add_honour"),

    # delete urls
    path("<int:edu_id>/delete_education/", DeleteEducationView.as_view(), name="delete_education"),
    path("<int:skl_id>/delete_skill/", DeleteSkillsView.as_view(), name="delete_skill"),
    path("<int:hon_id>/delete_honour/", DeleteHonourView.as_view(), name="delete_honour"),

    # update urls
    path("<int:skl_id>/update_skill/", UpdateSkillsView.as_view(), name="update_skill"),
    path("<int:edu_id>/update_education/", UpdateEducationView.as_view(), name="update_education"),
    path("<int:hon_id>/update_honour/", UpdateHonourView.as_view(), name="update_honour"),
]
