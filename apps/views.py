from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.models import Actor, Address, AuthGroup, AuthUser, Category, City, Country, Customer, Film, FilmActor, \
    FilmCategory, Inventory, Language, Payment, Rental, Staff, Store
from apps.serializer import ActorModelSerializer, AddressModelSerializer, AuthGroupModelSerializer, \
    AuthUserModelSerializer, CategoryModelSerializer, CityModelSerializer, CountryModelSerializer, \
    CustomerModelSerializer, FilmModelSerializer, FilmActorModelSerializer, FilmCategoryModelSerializer, \
    InventoryModelSerializer, LanguageModelSerializer, PaymentModelSerializer, RentalModelSerializer, \
    StaffModelSerializer, StoreModelSerializer


class ActorModelViewSet(ModelViewSet):
    queryset = Actor.objects.order_by('-last_update')
    serializer_class = ActorModelSerializer


class AddressModelViewSet(ModelViewSet):
    serializer_class = AddressModelSerializer


class AuthGroupModelViewSet(ModelViewSet):
    queryset = AuthGroup.objects.order_by('name')
    serializer_class = AuthGroupModelSerializer


class AuthUserModelViewSet(ModelViewSet):
    queryset = AuthUser.objects.order_by('-username')
    serializer_class = AuthUserModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.order_by('name')
    serializer_class = CategoryModelSerializer


class CountryModelViewSet(ModelViewSet):
    queryset = Country.objects.order_by('-last_update')
    serializer_class = CountryModelSerializer


class CityModelViewSet(ModelViewSet):
    queryset = City.objects.order_by('-last_update')
    serializer_class = CityModelSerializer


class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.order_by('-last_update')
    serializer_class = CustomerModelSerializer


class FilmModelViewSet(ModelViewSet):
    queryset = Film.objects.order_by('-release_year')
    serializer_class = FilmModelSerializer


class FilmActorModelViewSet(ModelViewSet):
    queryset = FilmActor.objects.order_by('-last_update')
    serializer_class = FilmActorModelSerializer


class FilmCategoryModelViewSet(ModelViewSet):
    queryset = FilmCategory.objects.order_by('-last_update')
    serializer_class = FilmCategoryModelSerializer


class InventoryModelViewSet(ModelViewSet):
    queryset = Inventory.objects.order_by('-last_update')
    serializer_class = InventoryModelSerializer


class LanguageModelViewSet(ModelViewSet):
    queryset = Language.objects.order_by('-last_update')
    serializer_class = LanguageModelSerializer


class PaymentModelViewSet(ModelViewSet):
    queryset = Payment.objects.order_by('-payment_date')
    serializer_class = PaymentModelSerializer


class RentalModelViewSet(ModelViewSet):
    queryset = Rental.objects.order_by('-rental_date')
    serializer_class = RentalModelSerializer


class StaffModelViewSet(ModelViewSet):
    queryset = Staff.objects.order_by('-last_update')
    serializer_class = StaffModelSerializer


class StoreModelViewSet(ModelViewSet):
    queryset = Store.objects.order_by('-last_update')
    serializer_class = StoreModelSerializer
