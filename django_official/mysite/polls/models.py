from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)


class IdcInfo(models.Model):
    virtual_choice = (
        (0, '否'),
        (1, '是'),
    )
    idc_name = models.CharField(max_length=50, verbose_name=(
        '机房名字'), default=u"", null=True, blank=True)
    is_virtual = models.IntegerField(verbose_name=(
        "是否云主机"), choices=virtual_choice, default=0)
