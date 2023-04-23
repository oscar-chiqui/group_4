from django.test import TestCase
from django.contrib.auth.models import User
from lmn.forms import NewNoteForm


class NoteTest(TestCase):
    
    def test_edit_notes_valid_form(self):
        
        valid_note = {
            'title': 'Diwali',
            'text': 'Bollywood Night'
        }
        form = NewNoteForm(valid_note)
        self.assertTrue(form.is_valid())
        
        