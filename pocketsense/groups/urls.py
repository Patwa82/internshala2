# groups/urls.py

from django.urls import path
from .views import GroupListCreateView, GroupMemberListView

urlpatterns = [
    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('group-members/', GroupMemberListView.as_view(), name='group-member-list-create'),
]
