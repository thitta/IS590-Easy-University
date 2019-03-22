from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    # use inbuilt RedirectView
    path('', RedirectView.as_view(pattern_name="courseinfo_section_list_urlpattern", permanent=False)),
    # use inbuilt TemplateView
    path('about/', TemplateView.as_view(template_name="courseinfo/about.html"), name="about_urlpattern"),
    path('admin/', admin.site.urls),
    path('', include("courseinfo.urls"))
]
