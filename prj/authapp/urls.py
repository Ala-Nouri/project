from django.urls import path
from .views import about, club_update,  clubs, contact, create_event, event, event_update, index, my_club, my_events, participant, signin, signout, signup



urlpatterns = [ 
    
    path('', index, name='home'),
    path('index/',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('clubs/',clubs,name='clubs'),
    path('event/<int:id>',event,name='event'),
    path('logout/', signout, name='signout'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('createvent/' ,create_event,name="create event"),
    path('myevent/<userid>' ,my_events,name="my event"),
    path('participant/<id>' ,participant,name="participant"),
    path('myclub/<id>', my_club, name='my club'),
    path('clubupdate/<id>' ,club_update,name="club_update"),
    path('eventupdate/<id>' ,event_update,name="event_update"),

]