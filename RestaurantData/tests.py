

# Create your tests here.
from django.test import TestCase
from .models import *

# class JobModelTests(TestCase):
# 	def test_job_name(self):
# 		new_job = Job(name='My job')
# 		print(new_job)
# 		self.assertIs(str(new_job), 'My job')

class Restaurant_typeModelTest(TestCase):
    def test_rest_type_description (self):
        new_desc = Restaurant_type(description='this is a test case')
        print(new_desc)
        self.assertIs(str(new_desc), 'this is a test case')