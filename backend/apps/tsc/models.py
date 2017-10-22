from datetime import datetime

from django.db import models


# Create your models here

class MSO(models.Model):
    mso_id = models.CharField(max_length=20, verbose_name="中控id")
    ip = models.GenericIPAddressField(unique=True, verbose_name="IP地址")
    department = models.CharField(max_length=30, verbose_name="设备归属部门")
    port = models.IntegerField(verbose_name="交换机连接端口")
    unit_type = models.CharField(max_length=20, null=True, blank=True, verbose_name="型号及其他")
    version = models.CharField(max_length=20, null=True, blank=True, verbose_name="使用版本")
    setup_time = models.DateField(default=datetime.now, verbose_name="搭建时间")
    principal = models.CharField(max_length=20, verbose_name="环境负责人")

    class Meta:
        verbose_name = "MSO"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}: {}".format("MSO", self.ip)


class TSC(models.Model):
    TSC_TYPE_CHOICES = {
        (1, "Large Clusters"),
        (2, "Small Clusters"),
    }
    tsc_id = models.CharField(max_length=20, verbose_name="基站id")
    ip = models.GenericIPAddressField(unique=True, verbose_name="IP地址")
    department = models.CharField(max_length=30, verbose_name="设备归属部门")
    port = models.IntegerField(verbose_name="交换机连接端口")
    carrier_num = models.IntegerField(verbose_name="载频数")
    unit_type = models.CharField(max_length=20, null=True, blank=True, verbose_name="型号及其他")
    version = models.CharField(max_length=20, null=True, blank=True, verbose_name="使用版本")
    setup_time = models.DateField(default=datetime.now, verbose_name="搭建时间")
    principal = models.CharField(max_length=20, verbose_name="环境负责人")
    tsc_type = models.IntegerField(choices=TSC_TYPE_CHOICES, verbose_name="集群类型")
    mso = models.ForeignKey(MSO, related_name="have_tsc", verbose_name="归属的中控")

    class Meta:
        verbose_name = "TSC"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}: {}".format("TSC", self.ip)


class DBS(models.Model):
    DBS_TYPE_CHOICES = {
        (1, "MySQL"),
        (2, "Oracle"),
    }
    ip = models.GenericIPAddressField(unique=True, verbose_name="IP地址")
    department = models.CharField(max_length=30, verbose_name="设备归属部门")
    port = models.IntegerField(verbose_name="交换机连接端口")
    unit_type = models.CharField(max_length=20, null=True, blank=True, verbose_name="型号及其他")
    version = models.CharField(max_length=20, null=True, blank=True, verbose_name="使用版本")
    setup_time = models.DateField(default=datetime.now, verbose_name="搭建时间")
    principal = models.CharField(max_length=20, verbose_name="环境负责人")
    dbs_type = models.IntegerField(choices=DBS_TYPE_CHOICES, verbose_name="数据库类型")
    mso = models.ForeignKey(MSO, related_name="have_dbs", verbose_name="归属的中控")

    class Meta:
        verbose_name = "DBS"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}: {}".format("DBS", self.ip)
