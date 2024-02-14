from django.contrib.gis.geos import MultiPolygon, Polygon, GEOSGeometry
from django.test import TestCase, Client
from django.urls import reverse
from ..models import VideoShapefile, GADMShapefile, GADMCountries, GADMProvinces, Polity, Capital
from ...general.models import Polity_capital
from ..views import get_polity_year_range, get_provinces, get_polity_info, get_polity_shape_content, get_all_polity_capitals
from ..templatetags.core_tags import get_polity_capitals, polity_map


# Simple square polygon to use in geospatial data table tests
square = MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
geo_square = GEOSGeometry(square).geojson

class ShapesTest(TestCase):
    """Test case for the shape models and views."""

    def setUp(self):
        """Set up the test client and Polity entry for the view functions."""
        self.client = Client()
        self.pk = 1
        self.polity = Polity.objects.create(
            name='TestPolity',
            id=self.pk,
            long_name='TestPolity',
            new_name='Test seshat_id'
        )
        self.video_shapefile = VideoShapefile.objects.create(
            geom=square,
            name="Test shape",
            polity="Testpolity",
            seshat_id="Test seshat_id",
            area=100.0,
            start_year=2000,
            end_year=2020,
            polity_start_year=2000,
            polity_end_year=2020,
            colour="#FFFFFF"
        )
        self.gadm_shapefile = GADMShapefile.objects.create(
            geom=square,
            UID=123456789,
            NAME_0="Test shape"
        )
        self.province = GADMProvinces.objects.create(
            geom=square,
            NAME_1="Test Province",
            ENGTYPE_1="Test Type"
        )
        self.country = GADMCountries.objects.create(
            geom=square,
            COUNTRY="Test Country"
        )
        self.capital = Capital.objects.create(
            name="Test Capital",
            latitude=51.567522,
            longitude=-0.1294531
        )
        self.polity_capital = Polity_capital.objects.create(
            name="Test Polity",
            capital="Test Capital",
            year_from=2000,
            year_to=2020,
            polity_id = self.pk
        )

    # Model tests

    def test_video_shapefile_creation(self):
        """Test the creation of a VideoShapefile instance."""
        self.assertIsInstance(self.video_shapefile, VideoShapefile)
        self.assertEqual(self.video_shapefile.name, "Test shape")

    def test_gadm_shapefile_creation(self):
        """Test the creation of a GADMShapefile instance."""
        self.assertIsInstance(self.gadm_shapefile, GADMShapefile)
        self.assertEqual(self.gadm_shapefile.NAME_0, "Test shape")

    def test_gadm_countries_creation(self):
        """Test the creation of a GADMCountries instance."""
        self.assertIsInstance(self.country, GADMCountries)
        self.assertEqual(self.country.COUNTRY, "Test Country")

    def test_gadm_provinces_creation(self):
        """Test the creation of a GADMProvinces instance."""
        self.assertIsInstance(self.province, GADMProvinces)
        self.assertEqual(self.province.NAME_1, "Test Province")

    # View function tests

    def test_get_polity_year_range(self):
        """Test the get_polity_year_range function."""
        expected_result = (2000, 2020)
        result = get_polity_year_range()
        self.assertEqual(result, expected_result)

    def test_get_provinces(self):
        """Test the get_provinces function."""
        province_result = get_provinces(selected_base_map_gadm='province', simplification_tolerance=0)
        country_result = get_provinces(selected_base_map_gadm='country', simplification_tolerance=0)
        
        province_expected_result = [{'aggregated_geometry': geo_square, 'province': 'Test Province', 'province_type': 'Test Type'}]
        country_expected_result = [{'aggregated_geometry': geo_square, 'country': 'Test Country'}]
        
        self.assertEqual(province_result, province_expected_result)
        self.assertEqual(country_result, country_expected_result)
        
    def test_get_polity_info(self):
        """Test the get_polity_info function."""
        seshat_ids = ['Test seshat_id']
        expected_result = [('Test seshat_id', 1, 'TestPolity')]
        result = get_polity_info(seshat_ids)
        self.assertEqual(result, expected_result)

    def test_get_polity_shape_content(self):
        """Test the get_polity_shape_content function."""
        expected_result = {
            'shapes': [
                {
                    'seshat_id': 'Test seshat_id',
                    'name': 'Test shape',
                    'start_year': 2000,
                    'end_year': 2020,
                    'polity_start_year': 2000,
                    'polity_end_year': 2020,
                    'colour': "#FFFFFF",
                    'area': 100.0,
                    'geom': geo_square
                }
            ],
            'earliest_year': 2000,
            'display_year': 2000,
            'latest_year': 2020,
            'seshat_id_page_id': {'Test seshat_id': {'id': 1, 'long_name': 'TestPolity'}}
        }
        result = get_polity_shape_content()
        self.assertEqual(result, expected_result)

    def test_get_polity_capitals(self):
        """Test the get_polity_capitals function."""
        result = get_polity_capitals(self.pk)
        self.assertEqual(result, [{'capital': 'Test Capital', 'latitude': 51.567522, 'longitude': -0.1294531}])
        
    def test_get_all_polity_capitals(self):
        """Test the get_all_polity_capitals function."""
        result = get_all_polity_capitals()
        self.assertEqual(result,
                        {'Test seshat_id': [
                                {'capital': 'Test Capital', 'latitude': 51.567522, 'longitude': -0.1294531}
                            ]
                        }
        )

    # def test_polity_map(self):
    #     """Test the polity_map template tag."""
    #     result = polity_map(self.pk)
    #     self.assertEqual(result['content']['include_polity_map'], True)

    # def test_map_view_initial(self):
    #     """Test the initial map view."""
    #     response = self.client.get(reverse('world_map'))
    #     self.assertEqual(response.status_code, 200)

    # def test_map_view_all(self):
    #     """Test the map view with all data."""
    #     response = self.client.get(reverse('world_map_all'))
    #     self.assertEqual(response.status_code, 200)

    # def test_provinces_and_countries_view(self):
    #     """Test the provinces and countries view."""
    #     response = self.client.get(reverse('provinces_and_countries'))
    #     self.assertEqual(response.status_code, 200)