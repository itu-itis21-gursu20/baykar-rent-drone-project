# from django.urls import reverse
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from django.contrib import auth

# User = get_user_model()

# class UserSignUpTests(TestCase):
#     def setUp(self):
#         self.username = "newuser"
#         self.password = "testpassword123"

#     def test_signup_page_url(self):
#         response = self.client.get("/signup/")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'signup.html')

#     def test_signup_form(self):
#         response = self.client.post(reverse('signup'), data={
#             'username': self.username,
#             'password1': self.password,
#             'password2': self.password
#         })
#         # Check that the user has been created
#         self.assertEqual(User.objects.count(), 1)
#         # Check that the user is redirected to the login page
#         self.assertRedirects(response, '/users/login')

# class UserLoginTests(TestCase):
#     def setUp(self):
#         self.username = "testuser"
#         self.password = "password"
#         User.objects.create_user(username=self.username, password=self.password)

#     def test_login_page_url(self):
#         response = self.client.get("/login/")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'login.html')

#     def test_login_form(self):
#         response = self.client.post(reverse('login'), data={
#             'username': self.username,
#             'password': self.password
#         })
#         # Check that the user is authenticated
#         user = auth.get_user(self.client)
#         self.assertTrue(user.is_authenticated)
#         # Check that the user is redirected to the home page
#         self.assertRedirects(response, '/drones/drones')
