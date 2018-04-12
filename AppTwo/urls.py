from django.conf.urls import url
from AppTwo import views

app_name = 'AppTwo'

# urlpatterns  = [

# 	url(r'^$',views.help,name = 'help'),
# 	url(r'^forms/',views.form_view,name='form_view')

# ]

urlpatterns = [

	url(r'^register/$' ,views.register,name='register' )
	


]