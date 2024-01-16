from django.urls import path
from .views import user_view, all_emp_view
urlpatterns = [
    path('<int:emp_id>/', user_view),
    path('all/', all_emp_view),
]
