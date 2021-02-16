from django.test import TestCase
from .models import Advert, CustomUser


class MockUser:
    is_authenticated = True


class BasicTest(TestCase):
    """
    Unit testing for LeMeilleurCoin
    """

    def setUp(self):
        """
        Create user for tests
        """
        self.user = CustomUser(username="Elliot", phone_number="+33646464646")
        self.user.set_password("P4$$w0rD")
        self.user.save()

    def test_user_creation(self):
        """
        Test manual user creation worked
        """
        data = CustomUser.objects.get(pk=self.user.pk)
        self.assertEqual(data, self.user)

    def test_advert_creation(self):
        """
        Test manual advert creation
        """
        self.advert = Advert.objects.create(
            title="Title",
            description="Some description",
            price=42,
            user=self.user,
        )
        data = Advert.objects.get(pk=self.advert.pk)
        self.assertEqual(self.advert, data)

    def test_login_view(self):
        """
        Test login view available without login
        """

        # Assert GET forbidden
        response = self.client.get("/login")
        self.assertEquals(response.status_code, 200)


class AuthTests(TestCase):
    def setUp(self):
        """
        Create user for tests
        """
        self.user = CustomUser(username="Elliot", phone_number="+33646464646")
        self.user.set_password("P4$$w0rD")
        self.user.save()

    def test_noauth_create_view(self):
        """
        Test CreateAdvert view unavailable without login
        """

        # Assert GET forbidden by redirect
        response = self.client.get("/adverts/new")
        self.assertRedirects(response, "/login?next=/adverts/new", 302)

        # Assert POST forbidden by redirect
        content = {
            "title": "Donkey",
            "description": "I am selling my donkey",
            "price": 666,
        }
        response = self.client.post("/adverts/new", content)
        self.assertRedirects(response, "/login?next=/adverts/new", 302)

    def test_noauth_list_view(self):
        """
        Test AdvertList view unavailable without login
        """

        # Assert GET forbidden by redirect
        response = self.client.get("/adverts/")
        self.assertRedirects(response, "/login?next=/adverts/", 302)

    def test_auth_list_view(self):
        """
        Test CreateAdvert view
        """

        # Login with user
        self.client.login(username="Elliot", password="P4$$w0rD")

        # Assert GET available
        response = self.client.get("/adverts/")
        self.assertEquals(response.status_code, 200)
        self.client.logout()

    def test_auth_detail_view(self):
        """
        Test AdvertDetail view available when logged in
        """
        advert = Advert.objects.create(
            title="Title",
            description="Some description",
            price=42,
            user=self.user,
        )

        # Login with user
        self.client.login(username="Elliot", password="P4$$w0rD")

        # Assert GET available
        response = self.client.get(f"/adverts/{advert.pk}")
        self.assertEquals(response.status_code, 200)
        self.client.logout()

    def test_auth_create_view(self):
        """
        Test CreateAdvert view
        """

        # Login with user
        self.client.login(username="Elliot", password="P4$$w0rD")

        # Post an advert as user
        content = {
            "title": "Donkey",
            "description": "I am selling my donkey",
            "price": 666,
        }
        response = self.client.post("/adverts/new", content)

        # Assert advert was created with proper content
        data = Advert.objects.get(description="I am selling my donkey")
        self.assertEqual(content["title"], data.title)
        self.assertEqual(content["description"], data.description)
        self.assertEqual(content["price"], data.price)
        self.assertEqual(data.user, self.user)

        # Assert creation view redirects to advert detail
        self.assertRedirects(response, f"/adverts/{data.pk}", 302)
        self.client.logout()

    def test_post_login_view(self):
        """
        Test login with correct user
        """

        content = {"username": "Elliot", "password": "P4$$w0rD"}
        response = self.client.post("/login", content)
        # Redirection means authentication worked
        self.assertRedirects(
            response, "/adverts", status_code=302, target_status_code=301
        )

    def test_post_bad_login_view(self):
        """
        Test login with correct user
        """

        content = {"username": "Elliot", "password": "wrongP4$$w0rD"}
        response = self.client.post("/login", content)
        # No redirection means authentication did not work
        self.assertEqual(response.status_code, 200)
