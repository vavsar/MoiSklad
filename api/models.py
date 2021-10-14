from django.db import models


class Ware(models.Model):
    # supplierArticle = models.CharField(max_length=10, unique=True)
    # photo = models.ImageField(blank=True)
    # SKU = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    # brand = models.CharField(max_length=50, blank=True)
    # color = models.CharField(max_length=20, blank=True)
    # category = models.CharField(max_length=20, blank=True)
    # seller = models.CharField(max_length=20, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    # number = models.CharField(max_length=20)
    # date = models.DateTimeField(auto_now_add=True)
    # lastChangedate = models.DateTimeField()
    supplierArticle = models.ForeignKey(Ware, on_delete=models.PROTECT, related_name='orders')
    # techSize = models.CharField(max_length=20)
    # barcode = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField()
    totalPrice = models.DecimalField(decimal_places=2, max_digits=10, blank=True, editable=False, null=True)
    discountPercent = models.PositiveSmallIntegerField(blank=True, null=True)
    # warehouseName = models.CharField(max_length=20)
    # oblast = models.CharField(max_length=20)
    # incomeID = models.PositiveIntegerField()
    # odid = models.PositiveIntegerField()
    # nmId = models.PositiveIntegerField()
    # subject = models.CharField(max_length=20)
    # category = models.CharField(max_length=20)
    # brand = models.CharField(max_length=20)
    # is_cancel = models.BooleanField()
    # cancel_dt = models.DateTimeField(auto_now_add=True)
    # gNumber = models.PositiveIntegerField()


class Sale(models.Model):
    # number = models.CharField(blank=True, null=True)
    # date = models.DateTimeField(auto_now_add=True)
    # lastChangedate = models.DateTimeField(blank=True, null=True)
    supplierArticle = models.ForeignKey(Ware, on_delete=models.PROTECT, related_name='sales')
    # techSize = models.CharField(max_length=20, blank=True)
    # barcode = models.CharField(max_length=20, blank=True)
    quantity = models.PositiveSmallIntegerField()
    totalPrice = models.DecimalField(decimal_places=2, max_digits=10, blank=True, editable=False, null=True)
    discountPercent = models.PositiveSmallIntegerField(blank=True, null=True)
    # isSupply = models.BooleanField(blank=True)
    # isRealization = models.BooleanField(blank=True)
    # orderId = models.PositiveIntegerField(blank=True, null=True)
    # promoCodeDiscount = models.PositiveSmallIntegerField(blank=True, null=True)
    # warehouseName = models.CharField(max_length=20, blank=True)
    # countryName = models.CharField(max_length=20, blank=True)
    # oblastOkrugName = models.CharField(max_length=20, blank=True)
    # regionName = models.CharField(max_length=20, blank=True)
    # incomeID = models.PositiveIntegerField(blank=True, null=True)
    # saleID = models.PositiveIntegerField(blank=True, null=True)
    # odid = models.PositiveIntegerField(blank=True, null=True)
    # spp = models.PositiveSmallIntegerField(blank=True, null=True)
    # forPay = models.DecimalField(decimal_places=2, max_digits=10, blank=True, editable=False, null=True)
    # finishedPrice = models.DecimalField(decimal_places=2, max_digits=10, blank=True, editable=False, null=True)
    priceWithDisc = models.DecimalField(decimal_places=2, max_digits=10, blank=True, editable=False, null=True)
    # nmId = models.PositiveIntegerField(blank=True, null=True)
    # subject = models.CharField(max_length=20, blank=True)
    # category = models.CharField(max_length=20, blank=True)
    # brand = models.CharField(max_length=20, blank=True)
    # IsStorno = models.BooleanField(blank=True)
    # gNumber = models.PositiveIntegerField(blank=True, null=True)



# class WareSale(models.Model):
#     sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
#     ware = models.ForeignKey(Ware, on_delete=models.CASCADE)
#     quantity = models.SmallIntegerField(default=1)



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


class Spp(models.Model):
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.amount}'
