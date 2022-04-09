from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from beerFridge.models import Beer


class TestApi(TestCase):

    def setUp(self):
        self.client=APIClient()
        self.getBeer_exists_url=reverse('beer', args=['ipa'])
        self.getBeer_does_not_exists_url=reverse('beer', args=['notvalid'])
        Beer.objects.create(

            type= "ipa",
            caloriesPerLiter= 330,
            color= "amber",
            alcoholPercentage= 6

            )

    #Testing the status codes for happy and sad requests
    def test_status_code_beer_by_type_GET(self):
        #test for a beer type that exists

        response=self.client.get(self.getBeer_exists_url)

        self.assertEquals(response.status_code,status.HTTP_200_OK)

        #test for a beer type that doesn't exist

        response=self.client.get(self.getBeer_does_not_exists_url)

        self.assertEquals(response.status_code,status.HTTP_404_NOT_FOUND)

    #Testing if the body is matching from happy case request
    def test_body_beer_by_type_GET(self):
    #get response
        response=self.client.get(self.getBeer_exists_url)

        #expected response
        ipa_dict={
            'id': 1,
            'type': 'ipa',
            'caloriesPerLiter':330,
            'color':'amber',
            'alcoholPercentage': 6

            }

        self.assertEquals(response.data,ipa_dict)
