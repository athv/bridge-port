
from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),  # initial request for page
    re_path(r"^signin/$", views.signin, name="signin"),
    re_path(
        r"^create_user/(?P<user_id>[0-9]+)/(?P<user_class>([a-z])+)$",
        views.create_new_user,
        name="new_user",
    ),
    re_path(r"^timetable/(?P<user_id>[0-9]+)$", views.get_timetable, name="timetable"),
    re_path(r"^notes/(?P<user_id>[0-9]+)$", views.get_notes, name="notes"),
    re_path(r"^subject_data/(?P<user_id>[0-9]+)$", views.get_sub_data, name="subject_data"),
    re_path(r"^events/(?P<user_id>[0-9]+)$", views.get_events, name="events"),
    re_path(r"^track_data/$", views.get_track_data, name="events"),
    re_path(r"^calendar/(?P<user_id>[0-9]+)$", views.get_cal_data, name="events"),
    re_path(
        r"^subject_attendence/(?P<user_id>[0-9]+)$",
        views.get_attendence,
        name="get_attendence",
    ),
    re_path(r"^create_user/$", views.create_new_user, name="new_user"),
    re_path(r"^update_attendence/$", views.update_attendence, name="update_attendence"),
    re_path(r"^set_track_data/$", views.set_track_data, name="set_track_data"),
]
