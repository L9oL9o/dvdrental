from pip._internal.cli.cmdoptions import list_exclude
from rest_framework.serializers import ModelSerializer

from apps.models import Actor, Address, AuthGroup, AuthUser, Category, City, Country, Customer, Film, FilmActor, \
    FilmCategory, Inventory, Language, Payment, Rental, Staff, Store


class ActorModelSerializer(ModelSerializer):
    class Meta:
        model = Actor
        exclude = ()


class AddressModelSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ()


class AuthGroupModelSerializer(ModelSerializer):
    class Meta:
        model = AuthGroup
        exclude = ()


class AuthUserModelSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        exclude = ()


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class CityModelSerializer(ModelSerializer):
    class Meta:
        model = City
        exclude = ()


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        exclude = ()


class CustomerModelSerializer(ModelSerializer):
    class Meta:
        model = Customer
        exclude = ()


class FilmModelSerializer(ModelSerializer):
    class Meta:
        model = Film
        exclude = ()


class FilmActorModelSerializer(ModelSerializer):
    class Meta:
        model = FilmActor
        exclude = ()


class FilmCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = FilmCategory
        exclude = ()


class InventoryModelSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        exclude = ()


class LanguageModelSerializer(ModelSerializer):
    class Meta:
        model = Language
        exclude = ()


class PaymentModelSerializer(ModelSerializer):
    class Meta:
        model = Payment
        exclude = ()


class RentalModelSerializer(ModelSerializer):
    class Meta:
        model = Rental
        exclude = ()


class StaffModelSerializer(ModelSerializer):
    class Meta:
        model = Staff
        exclude = ()


class StoreModelSerializer(ModelSerializer):
    class Meta:
        model = Store
        exclude = ()
