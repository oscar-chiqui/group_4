from django.urls import path
from django.contrib.auth import views as auth_views

from .views import views_main, views_artists, views_venues, views_notes, views_users, views_shows


urlpatterns = [

    path('', views_main.homepage, name='homepage'),

    # Venue related URLs
    path('venues/list/', views_venues.venue_list, name='venue_list'),
    path('venues/detail/<int:venue_pk>/', views_venues.venue_detail, name='venue_detail'),
    path('venues/artists_at/<int:venue_pk>/', views_venues.artists_at_venue, name='artists_at_venue'),

    # Note related URLs
    path('notes/latest/', views_notes.latest_notes, name='latest_notes'),
    path('notes/detail/<int:note_pk>/', views_notes.note_detail, name='note_detail'),
    path('notes/for_show/<int:show_pk>/', views_notes.notes_for_show, name='notes_for_show'),
    path('notes/add/<int:show_pk>/', views_notes.new_note, name='new_note'),
    path('notes/delete/<int:note_pk>/', views_notes.delete_note, name='delete_note'),
    path('notes/delete_confirmation/<int:note_pk>', views_notes.delete_confirmation, name='delete_confirmation'),
    path('notes/edit/<int:note_pk>/', views_notes.edit_note, name='edit_note'),
    path('notes/search/', views_notes.search_notes, name='search_notes'), # A path for search_notes
    
    # Artist related URLs
    path('artists/list/', views_artists.artist_list, name='artist_list'),
    path('artists/detail/<int:artist_pk>/', views_artists.artist_detail, name='artist_detail'),
    path('artists/venues_played/<int:artist_pk>/', views_artists.venues_for_artist, name='venues_for_artist'),

    # Show related URLS
    path('shows/most_notes_list/', views_shows.shows_with_most_notes, name='shows_with_most_notes'),

    # User related URLs
    path('user/profile/<int:user_pk>/', views_users.user_profile, name='user_profile'),
    path('user/profile/', views_users.my_user_profile, name='my_user_profile'),
    path('user/edit_account_info/<int:user_pk>/', views_users.edit_user_account_info, name='edit_user_account_info'),
    path('user/change_password/<int:user_pk>/', views_users.change_user_password, name='change_user_password'),

    # Account related URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views_users.register, name='register'),

]
