import requests
import pytest

BASE_URL = "https://cloud-api.yandex.net/v1/disk"
TOKEN = ""  # Токен от яндекс-диска
HEADERS = {
    "Authorization": f"OAuth {TOKEN}",
    "Content-Type": "application/json"
}

def create_test_folder(folder_name: str) -> requests.Response:
    url = f"{BASE_URL}/resources"
    params = {"path": folder_name}
    response = requests.put(url, headers=HEADERS, params=params)
    return response

def delete_test_folder(folder_name: str) -> requests.Response:
    url = f"{BASE_URL}/resources"
    params = {"path": folder_name}
    response = requests.delete(url, headers=HEADERS, params=params)
    return response

def folder_exists(folder_name: str) -> bool:
    url = f"{BASE_URL}/resources"
    params = {"path": folder_name}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.status_code == 200

class TestYandexDiskFolderCreation:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.test_folder = "TestFolder"
        yield
        delete_test_folder(self.test_folder)

    def test_create_folder_success(self):
        response = create_test_folder(self.test_folder)
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}: {response.text}"
        assert folder_exists(self.test_folder), "Папка не появилась в списке файлов"

    def test_create_existing_folder(self):
        create_test_folder(self.test_folder)
        response = create_test_folder(self.test_folder)
        assert response.status_code == 409, f"Ожидался код 409, получен {response.status_code}"

    def test_create_folder_unauthorized(self):
        url = f"{BASE_URL}/resources"
        params = {"path": self.test_folder}
        response = requests.put(url, params=params)
        assert response.status_code == 401, f"Ожидался код 401, получен {response.status_code}"
