# groups/views.py

from rest_framework import generics
from .models import Group, GroupMember
from .serializers import GroupSerializer, GroupMemberSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrMember

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create or view groups

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GroupMemberListView(generics.ListCreateAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [IsAdminOrMember]

    def perform_create(self, serializer):
        # Automatically add the current user to the group as a member
        serializer.save(user=self.request.user)
