from django.test import TestCase
from .models import itemlost, itemfound
from django.urls import reverse

class LostAndFoundTestCase(TestCase):
    def setUp(self):
        self.lost_item = itemlost.objects.create(
            product_title="Lost Phone",
            place="Near the park",
            date="2023-01-10",
            time="10:00:00",
            description="Black smartphone",
            contactme="user@example.com",
            username="user1",
        )

        self.found_item = itemfound.objects.create(
            product_title="Found Wallet",
            place="In a cafe",
            date="2023-01-15",
            time="14:30:00",
            description="Brown leather wallet",
            contactme="user@example.com",
            username="user2",
        )

    def test_lost_item_creation(self):
        self.assertEqual(self.lost_item.product_title, "Lost Phone")

    def test_found_item_creation(self):
        self.assertEqual(self.found_item.product_title, "Found Wallet")

    def test_lost_item_search_view(self):
        response = self.client.get(reverse('lost_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lost Phone")

    def test_found_item_search_view(self):
        response = self.client.get(reverse('found_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Found Wallet")



