from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('cart/', include('cart.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('order/', include("order.urls")),
                  path('', include('core.urls')),
                  path('our/story/', TemplateView.as_view(template_name="pages/our-story.html"), name='our_story')

              ] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
