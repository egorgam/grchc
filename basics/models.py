from django.db import models
from django.utils.translation import gettext_lazy as _


class T_1(models.Model):
    name = models.CharField(max_length=10)
    responsible_group = models.ManyToManyField(
        "auth.Group",
    )

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = _("ПМ1")
        verbose_name_plural = _("ПМ1")


class T_2(models.Model):
    name = models.CharField(max_length=10)
    responsible_group = models.ManyToManyField(
        "auth.Group",
    )

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = _("ПМ2")
        verbose_name_plural = _("ПМ2")


class T_3(models.Model):
    name = models.CharField(max_length=10)
    responsible_group = models.ManyToManyField(
        "auth.Group",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("ПМ3")
        verbose_name_plural = _("ПМ3")
