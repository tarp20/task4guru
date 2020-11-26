from .utils import is_car_exist
from django.test import TestCase
from rest_framework.test import ApiTestCase
from rest_framework import status


.models import Car, Rating


class TestCarViewSet(ApiTestCase):
    def test_post_car(self):
        response = self.client.post(
            '/cars/', {"Make_Name": "BMW", "Model_Name": "i3"})
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_cars(self):
        Car.objects.create(**{"Make_Name": "Test name",
                           "Model_Name": "Model test"})
        Car.objects.create(**{"Make_Name": "Test name",
                           "Model_Name": "Model test"})

        response = self.client.get('api/cars/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Car.objects.count(), 2)

        self.assertEqual(Car.objects.get(id=3).Model_Name, "Model test")
        self.assertEqual(Car.objects.get(id=4).Make_Name, "Test name")


class TestRatingViewSet(ApiTestCase):
    def setUp(self):
        Movie.objects.create({"Make_Name1": "Test name",
                           "Model_Name": "Model test"})

    def test_get_ratings(self):
        response1 = self.client.post('api/rate/', {"car": 2, "content": 5})
        response2 = self.client.post('api/rate/', {"car": 2, "content": 3})
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response1.data['content'], 5)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.data['content'], 3)
        self.assertEqual(Rating.objects.count(), 2)


class TestCarsPopularViewSet(ApiTestCase):
        def setUp(self):
        Car.objects.create({"Make_Name1": "Test name",
                           "Model_Name": "Model test"})
        Car.objects.create({"Make_Name2": "Test name",
                           "Model_Name": "Model test"})
        Car.objects.create({"Make_Name3": "Test name",
                           "Model_Name": "Model test"})
        Car.objects.get(id=6).ratings.create(**{"content": 2})
        Car.objects.get(id=6).ratings.create(**{"content": 5})
        Car.objects.get(id=7).ratings.create(**{"content": 5})
        Car.objects.get(id=8).ratings.create(**{"content": 2})

    def test_get_top(self):
        response = self.client.get('api/popular/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['total_rating'], 2)

        self.assertEqual(response.data[1]['total_ratings'], 1)
         
        self.assertEqual(response.data[2]['total_ratings'], 1)








    
