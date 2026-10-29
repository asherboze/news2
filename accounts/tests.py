from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        _assert_superuser_created(self)


def _assert_superuser_created(test_case):
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        username="testsuperuser",
        email="testsuperuser@example.com",
        password="testpass1234",
    )
    test_case.assertEqual(admin_user.username, "testsuperuser")
    test_case.assertEqual(admin_user.email, "testsuperuser@example.com")
    test_case.assertTrue(admin_user.is_active)
    test_case.assertTrue(admin_user.is_staff)
    test_case.assertTrue(admin_user.is_superuser)
