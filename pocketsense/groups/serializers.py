# groups/serializers.py

from rest_framework import serializers
from .models import Group, GroupMember
from users.models import CustomUser

class GroupSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    members = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'created_by', 'members']

class GroupMemberSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = GroupMember
        fields = ['group', 'user', 'joined_at']
