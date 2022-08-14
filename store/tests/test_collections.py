from rest_framework.test import APIClient
from rest_framework import status

class TestCreateCollection:
    def test_if_user_is_anonymouse_return_401(self):
        # arrange

        #act
        client = APIClient()
        response = client.post("/store/collections/",{'title': 'a'})

        # assert        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED