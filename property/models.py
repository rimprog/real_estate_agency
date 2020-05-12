from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField("ФИО владельца", max_length=200, db_index=True)
    owners_phonenumber = models.CharField("Номер владельца", max_length=20, db_index=True)
    owner_phone_pure = PhoneNumberField("Нормализованый номер владельца", blank=True, db_index=True)
    created_at = models.DateTimeField("Когда создано объявление", default=timezone.now, db_index=True)

    description = models.TextField("Текст объявления", blank=True)
    price = models.IntegerField("Цена квартиры", db_index=True)

    town = models.CharField("Город, где находится квартира", max_length=50, db_index=True)
    town_district = models.CharField("Район города, где находится квартира", max_length=50, blank=True, help_text='Чертаново Южное')
    address = models.TextField("Адрес квартиры", help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField("Этаж", max_length=3, help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField("Количество комнат в квартире", db_index=True)
    living_area = models.IntegerField("количество жилых кв.метров", null=True, blank=True, db_index=True)

    has_balcony = models.NullBooleanField("Наличие балкона", db_index=True)
    active = models.BooleanField("Активно-ли объявление", db_index=True)
    construction_year = models.IntegerField("Год постройки здания", null=True, blank=True, db_index=True)
    new_building = models.NullBooleanField("Новостройка", db_index=True)

    liked_by = models.ManyToManyField(
        User,
        verbose_name='кто лайкнул',
        related_name='liked_flats',
        blank=True
    )

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"


class Owner(models.Model):
    full_name = models.CharField("ФИО владельца", max_length=200, db_index=True)
    owner_phonenumber = models.CharField("Номер владельца", max_length=20, db_index=True)
    owner_phone_pure = PhoneNumberField("Нормализованый номер владельца", blank=True, db_index=True)
    flats = models.ManyToManyField(
        Flat,
        verbose_name='квартиры',
        related_name='owners',
        db_index=True
    )


class Complaint(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='кто жаловался',
        related_name='complaints',
        on_delete=models.SET_NULL,
        null=True,
    )
    flat = models.ForeignKey(
        Flat,
        verbose_name='квартира на которую пожаловались',
        related_name='complaints',
        on_delete=models.SET_NULL,
        null=True,
    )
    text = models.TextField('текст жалобы', max_length=500, db_index=True)
