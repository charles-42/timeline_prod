from django.test import TestCase

from story.models import Events

class EventsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Events.objects.create(date=1789, period=26, name='révolution française', comment='un grand événement', category='HI',theme='',wiki='')

        # test that name field doesn't exceed 200 characters. 
    def test_name_max_length(self):
        event = Events.objects.get(id=1)
        max_length = event._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
