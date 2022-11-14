from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username='test',
            email='sobaka@mail.ru',
            password='12345q35we_r7ty678'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'sobaka@mail.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            username='superuser',
            email='spsp@yandex.ru',
            password='138456^23_4r5b&6d7mm9fv8e7e65'
        )
        self.assertEqual(admin_user.username, 'superuser')
        self.assertEqual(admin_user.email, 'spsp@yandex.ru')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

