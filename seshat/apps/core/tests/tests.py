from django.test import TestCase
from ..models import VideoShapefile, GADMShapefile, GADMCountries, GADMProvinces
from ..views import map_view_initial, map_view_all, provinces_and_countries_view

# Create your tests here.
class ModelTest(TestCase):
    def test_video_shapefile_creation(self):
        video_shapefile = VideoShapefile.objects.create(name="Test Video")
        self.assertIsInstance(video_shapefile, VideoShapefile)
        self.assertEqual(video_shapefile.name, "Test Video")

    def test_gadm_shapefile_creation(self):
        gadm_shapefile = GADMShapefile.objects.create(name="Test GADM")
        self.assertIsInstance(gadm_shapefile, GADMShapefile)
        self.assertEqual(gadm_shapefile.name, "Test GADM")

    def test_gadm_countries_creation(self):
        gadm_countries = GADMCountries.objects.create(name="Test Country")
        self.assertIsInstance(gadm_countries, GADMCountries)
        self.assertEqual(gadm_countries.name, "Test Country")

    def test_gadm_provinces_creation(self):
        gadm_provinces = GADMProvinces.objects.create(name="Test Province")
        self.assertIsInstance(gadm_provinces, GADMProvinces)
        self.assertEqual(gadm_provinces.name, "Test Province")

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_map_view_initial(self):
        response = self.client.get(reverse('core/world_map/'))
        self.assertEqual(response.status_code, 200)

    def test_map_view_all(self):
        response = self.client.get(reverse('core/world_map_all/'))
        self.assertEqual(response.status_code, 200)

    def test_provinces_and_countries_view(self):
        response = self.client.get(reverse('core/provinces_and_countries'))
        self.assertEqual(response.status_code, 200)