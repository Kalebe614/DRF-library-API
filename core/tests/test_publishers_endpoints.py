from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import PublisherModel
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from model_mommy import mommy
from django.forms.models import model_to_dict

class PublishersListAPITestCase(APITestCase):

    def setUp(self):

       self.publisher1 = mommy.make(PublisherModel)
       self.publisher2 = mommy.make(PublisherModel)

    def test_list_publishers_returns_all(self):

        url = reverse('publishers-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data),2)

        self.assertEqual(response.data[0]['name'], self.publisher1.name)
        self.assertEqual(response.data[0]['description'], self.publisher1.description)

class PublisherCreateAPITestCase(APITestCase):
    
        def setUp(self):
             
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)  

        def test_create_publisher(self):
            url = reverse('publishers-list')

            data = {
                'name': 'New Publisher',
                'description': 'New Description'
            }

            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
            response = self.client.post(url, data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            self.assertEqual(response.data['name'], data['name'])
            self.assertEqual(response.data['description'], data['description'])

            publisher = PublisherModel.objects.get(name=data['name'])
            self.assertEqual(publisher.description, data['description'])


class PublisherDeleteAPITestCase(APITestCase):

        def setUp(self):
   
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)
        
            self.publisher1 = mommy.make(PublisherModel)

        def test_delete_publisher(self):
             
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
            
            url = reverse('publishers-detail', kwargs={'pk': self.publisher1.pk})

            response = self.client.delete(url)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      
            self.assertFalse(PublisherModel.objects.filter(pk=self.publisher1.pk).exists())

class PublisherUpdateAPITestCase(APITestCase):

        def setUp(self):
            
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)
            self.publisher1 = mommy.make(PublisherModel)

        def test_update_publisher(self):
            print(self.publisher1.pk)
            self.publisherUpdated = mommy.make(PublisherModel)
            print(self.publisherUpdated.pk)
            url = reverse('publishers-detail', kwargs={'pk': self.publisher1.pk})

            self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ str(self.token))

            data = model_to_dict(self.publisherUpdated)

            response = self.client.put(url, data)

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            self.publisher1.refresh_from_db()
            self.assertEqual(self.publisher1.name, self.publisherUpdated.name)


class PublisherDetailAPITestCase(APITestCase):

        def setUp(self):
            self.user = User.objects.create_user(username='newuser', password='exampleTestPassword')
            self.token = AccessToken.for_user(self.user)  
            self.publisher1 = mommy.make(PublisherModel)

        def test_detail_publisher(self):
             
           
            url = reverse('publishers-detail', kwargs={'pk': self.publisher1.pk})

            self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ str(self.token))
            
            response = self.client.get(url)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
      
            self.assertEqual(response.data['name'], self.publisher1.name)
            self.assertEqual(response.data['description'], self.publisher1.description)
