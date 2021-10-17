from rest_framework.test import APITransactionTestCase
from rest_framework import status

class TestAPI(APITransactionTestCase):
    def test_default(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_query_string_page(self):
        response = self.client.get("/api/users/?page=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_query_string_size(self):
        response = self.client.get("/api/users/?size=15")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_string_page_size(self):
        response = self.client.get("/api/users/?page=2&size=15")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_string_region(self):
        response = self.client.get("/api/users/?region=sul")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_string_type(self):
        response = self.client.get("/api/users/?type=laborious")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_string_region_type(self):
        response = self.client.get("/api/users/?region=sul&type=laborious")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_query_string_page(self):
        response = self.client.get("/api/users/?page=random")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_query_string_size(self):
        response = self.client.get("/api/users/?size=random")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)