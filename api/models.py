from django.db import models


class Ware(models.Model):
    supplierArticle = models.PositiveIntegerField()
    photo = models.ImageField()
    SKU = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    seller = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField()

    def __str__(self):
        return self.supplierArticle


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class WarenHouse(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Oblast(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    lastChangedate = models.DateTimeField()
    supplierArticle = models.ForeignKey(Ware, on_delete=models.PROTECT)
    techSize = models.CharField(max_length=20)
    barcode = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField()
    totalPrice = models.IntegerField()
    discountPercent = models.PositiveSmallIntegerField()
    warehouseName = models.CharField(max_length=20)
    oblast = models.CharField(max_length=20)
    incomeID = models.PositiveIntegerField()
    odid = models.PositiveIntegerField()
    nmId = models.PositiveIntegerField()
    subject = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    is_cancel = models.BooleanField()
    cancel_dt = models.DateTimeField(auto_now_add=True)
    gNumber = models.PositiveIntegerField()


class Sale(models.Model):
    number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    lastChangedate = models.DateTimeField()
    supplierArticle = models.ForeignKey(Ware, on_delete=models.PROTECT)
    techSize = models.CharField(max_length=20)
    barcode = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField()
    totalPrice = models.IntegerField()
    discountPercent = models.PositiveSmallIntegerField()
    isSupply = models.BooleanField()
    isRealization = models.BooleanField()
    orderId = models.PositiveIntegerField()
    promoCodeDiscount = models.PositiveSmallIntegerField()
    warehouseName = models.CharField(max_length=20)
    countryName = models.CharField(max_length=20)
    oblastOkrugName = models.CharField(max_length=20)
    regionName = models.CharField(max_length=20)
    incomeID = models.PositiveIntegerField()
    saleID = models.PositiveIntegerField()
    odid = models.PositiveIntegerField()
    spp = models.PositiveSmallIntegerField()
    forPay = models.DecimalField()
    finishedPrice = models.DecimalField()
    priceWithDisc = models.DecimalField()
    nmId = models.PositiveIntegerField()
    subject = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    IsStorno = models.BooleanField()
    gNumber = models.PositiveIntegerField()


