from django.test import TestCase
# from .models import Course

# Create your tests here.

class CourseTestCase(TestCase):
    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass
    #     # Course.objects.create(name="course1", credit=10)
    #     # Course.objects.create(name="course2", credit=20)
    #
    # def sample_test(self):
    #     """sample test"""
    #     # course1 = Course.objects.get(name="course1")
    #     # course2 = Course.objects.get(name="course2")
    #     # self.assertEqual(course1 != course2, True)
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)



