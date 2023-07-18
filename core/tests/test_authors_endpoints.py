from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import AuthorModel
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from model_mommy import mommy
from django.forms.models import model_to_dict

class AuthorListAPITestCase(APITestCase):

    def setUp(self):

        self.author1 = mommy.make(AuthorModel)
        self.author2 = mommy.make(AuthorModel)
    def test_list_authors_returns_all(self):

        url = reverse('authors-list')
        data = model_to_dict(self.author1)
        response = self.client.get(url,data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data),2)

        self.assertEqual(response.data[0]['first_name'], self.author1.first_name)
        self.assertEqual(response.data[0]['last_name'], self.author1.last_name)
        self.assertEqual(response.data[0]['about'], self.author1.about)

class AuthorCreateAPITestCase(APITestCase):
    
        def setUp(self):
             
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)  

        def test_create_author(self):

            self.author1 = mommy.make(AuthorModel)
            url = reverse('authors-list')
            data = model_to_dict(self.author1)
           
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
            response = self.client.post(url, data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            self.assertEqual(response.data['first_name'], data['first_name'])
            self.assertEqual(response.data['last_name'], data['last_name'])
            self.assertEqual(response.data['about'], data['about'])

            
class AuthorDeleteAPITestCase(APITestCase):

        def setUp(self):
   
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)
        
            self.author1 = mommy.make(AuthorModel)

        def test_delete_author(self):
             
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
            
            url = reverse('authors-detail', kwargs={'pk': self.author1.pk})

            response = self.client.delete(url)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      
            self.assertFalse(AuthorModel.objects.filter(pk=self.author1.pk).exists())

class AuthorUpdateAPITestCase(APITestCase):

        def setUp(self):
            
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)
            self.author1 = mommy.make(AuthorModel)

        def test_update_author(self):

            self.authorUpdated = mommy.make(AuthorModel)

            url = reverse('authors-detail', kwargs={'pk': self.author1.pk})

            self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ str(self.token))

            data = model_to_dict(self.authorUpdated)

            response = self.client.put(url, data)

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            self.author1.refresh_from_db()
            self.assertEqual(self.author1.first_name, self.authorUpdated.first_name)


class AuthorDetailAPITestCase(APITestCase):

        def setUp(self):
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)  
            self.author1 = mommy.make(AuthorModel)

        def test_detail_author(self):
             
           
            url = reverse('authors-detail', kwargs={'pk': self.author1.pk})

            self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ str(self.token))
            
            response = self.client.get(url)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
      
            self.assertEqual(response.data['first_name'], self.author1.first_name)
            self.assertEqual(response.data['last_name'], self.author1.last_name)
            self.assertEqual(response.data['about'], self.author1.about)
