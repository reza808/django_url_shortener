from django.urls import re_path
from .views import URLRedirectView


urlpatterns = [
    re_path(r"^(?P<shortcode>[\w-]+)/$", URLRedirectView.as_view(), name="scode"),
]
