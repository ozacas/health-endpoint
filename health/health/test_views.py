from django.test import TestCase
from health import views
from rest_framework.test import APIClient
import mock
import json


class TestRun(TestCase):
    def test_success(self):
        stdout = views.run(["/bin/ls", "-1", "/bin/ls"])
        self.assertEqual(stdout, b"/bin/ls")

    def test_expected_fail(self):
        stdout = views.run("/not/existing")
        self.assertEqual(stdout, "n/a")
        stdout = views.run("/not/existing", shell=True)
        self.assertEqual(stdout, "n/a")


class TestAPIView(TestCase):
    factory = APIClient()

    @mock.patch("health.views.app_name")
    @mock.patch("health.views.git_most_recent_tag")
    @mock.patch("health.views.git_hash")
    def test_success(self, mock_hash, mock_ver, mock_name):
        mock_name.return_value = "test_app"
        mock_ver.return_value = "v0.0.0"
        mock_hash.return_value = "test_hash"
        expected_result = {
            "git hash": "test_hash",
            "app name": "test_app",
            "app version": "v0.0.0",
        }

        resp = self.factory.get("/health", format="json")

        self.assertEqual(resp.status_code, 200)

        self.assertEqual(json.loads(resp.content.decode("utf-8")), expected_result)
