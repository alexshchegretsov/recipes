from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModel(TestCase):

    def test_create_user_model_with_email_and_password(self):
        """Test creating model with an email and password"""
        email = 'foo@bazzbar.com'
        password = 'test123456'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized(self):
        """Test email is normalized after user creation"""
        email = 'foo@BYZZ.COM'
        user = get_user_model().objects.create_user(email=email, password='ere')
        self.assertEqual(user.email, email.lower())

    def test_user_email_is_invalid(self):
        """Test error on user creating if no valid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='ere')
