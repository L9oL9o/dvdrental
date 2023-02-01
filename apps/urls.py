from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ActorModelViewSet, AddressModelViewSet, AuthGroupModelViewSet, AuthUserModelViewSet, \
    CategoryModelViewSet, CountryModelViewSet, CityModelViewSet, CustomerModelViewSet, FilmModelViewSet, \
    FilmActorModelViewSet, FilmCategoryModelViewSet, InventoryModelViewSet, LanguageModelViewSet, PaymentModelViewSet, \
    RentalModelViewSet, StaffModelViewSet, StoreModelViewSet

router = DefaultRouter()
router.register('actor', ActorModelViewSet, 'actor')
router.register('address', AddressModelViewSet, 'address')
router.register('auth-group', AuthGroupModelViewSet, 'auth-group')
router.register('auth-user', AuthUserModelViewSet, 'auth-user')
router.register('category', CategoryModelViewSet, 'category')
router.register('country', CountryModelViewSet, 'country')
router.register('city', CityModelViewSet, 'city')
router.register('customer', CustomerModelViewSet, 'customer')
router.register('film', FilmModelViewSet, 'film')
router.register('film-actor', FilmActorModelViewSet, 'film-actor')
router.register('film-category', FilmCategoryModelViewSet, 'film-category')
router.register('inventory', InventoryModelViewSet, 'inventory')
router.register('language', LanguageModelViewSet, 'language')
router.register('payment', PaymentModelViewSet, 'payment')
router.register('rental', RentalModelViewSet, 'rental')
router.register('staff', StaffModelViewSet, 'staff')
router.register('store', StoreModelViewSet, 'store')

urlpatterns = [
    path('router-url/', include(router.urls)),
]
