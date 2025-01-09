# groups/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Group, GroupMember
from users.models import CustomUser

class GroupTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(username='testuser1', password='password123')
        self.user2 = CustomUser.objects.create_user(username='testuser2', password='password123')
        self.group_data = {
            'name': 'Test Group',
            'members': [self.user1.id, self.user2.id],
        }
        self.group = Group.objects.create(name='Test Group', created_by=self.user1)
        GroupMember.objects.create(group=self.group, user=self.user1)
        GroupMember.objects.create(group=self.group, user=self.user2)

    def test_create_group(self):
        response = self.client.post('/api/groups/', self.group_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_member_to_group(self):
        member_data = {'group': self.group.id, 'user': self.user2.id}
        response = self.client.post('/api/group-members/', member_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_permissions_for_non_member(self):
        # Create a new user who is not a member of the group
        user3 = CustomUser.objects.create_user(username='testuser3', password='password123')
        self.client.force_authenticate(user=user3)
        response = self.client.get(f'/api/groups/{self.group.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
