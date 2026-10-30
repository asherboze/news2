from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
        )

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password("testpass123"))

    def test_create_superuser(self):
        admin_user = get_user_model().objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass123",
        )

        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.check_password("testpass123"))


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")

        self.assertEqual(response.status_code, 200)

    def test_signup_view_by_name(self):
        response = self.client.get(reverse("signup"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form_creates_user(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "signupuser",
                "email": "signupuser@example.com",
                "age": 25,
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("login"),
            fetch_redirect_response=False,
        )

        user = get_user_model().objects.get(username="signupuser")
        self.assertEqual(user.email, "signupuser@example.com")
        self.assertEqual(user.age, 25)
        self.assertTrue(user.check_password("testpass123"))
