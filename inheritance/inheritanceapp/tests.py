from django.test import TestCase
from models import Artifact

'''
POSSIBLE TESTS
- are artifacts added to gallery as expected with correct data displaying?
- if user doesn't select category, is user required to do so before can proceed?
- when an artifact is added to the gallery, is the user re-directed to the gallery page?
'''

# Create your tests here.
@classmethod
def add_artifact(cls):
    cls.artifact = Artifact.objects.created(
    imgtitle ='Raw Effort', 
    imgdesc ='against odds to success', 
    category ='artistic'
    )
    # return "Artifact added! Gallery not empty!"

class TestAddArtifact(TestCase):
    def test_add_artifact(self):
        self.assertEqual(add_artifact(), )
        self.assertEqual(len(form.fields), 3)
        self.assertIn('imgtitle', form.fields)
        self.assertIn('imgdesc', form.fields)
        self.assertIs('category', True)

# def error_when_category_not_selected():
#     return "Category not selected! Artifact not added to gallery!"

# class TestErrorWhenCategoryNotSelected(TestCase):
#     def test_error_when_category_not_selected(self):
#         self.assertFalse(error_when_category_not_selected(), )

