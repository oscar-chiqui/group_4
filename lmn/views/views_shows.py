from django.shortcuts import render
from django.db.models import Count

from ..models import Show


def shows_with_most_notes(request):
    """ Get the the Shows with the top ten count of notes.
    Also, get all of the notes associated with each Show. """

    # Get the top ten shows with the most notes by getting the count and ordering by number of notes. 
    top_10_shows = Show.objects.annotate(num_notes=Count('note')).order_by('-num_notes')[:10]  # Adapted from Django docs https://docs.djangoproject.com/en/4.2/topics/db/aggregation/
    
    for show in top_10_shows:
        show.notes = show.note_set.all() # Get data on the Note objects associated with each Show

    return render(request, 'lmn/shows/shows_with_most_notes.html', {'top_10_shows': top_10_shows})