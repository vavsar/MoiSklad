import json
import copy

with open('Продажи.json', encoding="utf8") as dataf, open('data.json',
                                                          'w') as out:
    data = json.load(dataf)
    newdata = []
    for i, block in enumerate(data):
        new = dict(model="wares.sale", pk=i + 1)
        new['fields'] = dict(
            number=block['number'],
            date=block['date'],
            lastChangeDate=block['lastChangeDate'],
            supplierArticle=block['supplierArticle'],
            techSize=block['techSize'],
            barcode=block['barcode'],
            quantity=block['quantity'],
            totalPrice=block['totalPrice'],
            discountPercent=block['discountPercent'],
            isSupply=block['isSupply'],
            isRealization=block['isRealization'],
            orderId=block['orderId'],
            promoCodeDiscount=block['promoCodeDiscount'],
            warehouseName=block['warehouseName'],
            countryName=block['countryName'],
            oblastOkrugName=block['oblastOkrugName'],
            regionName=block['regionName'],
            incomeID=block['incomeID'],
            saleID=block['saleID'],
            odid=block['odid'],
            spp=block['spp'],
            forPay=block['forPay'],
            finishedPrice=block['finishedPrice'],
            priceWithDisc=block['priceWithDisc'],
            nmId=block['nmId'],
            subject=block['subject'],
            category=block['category'],
            brand=block['brand'],
            IsStorno=block['IsStorno'],
            gNumber=block['gNumber'],
        )
        newdata.append(copy.deepcopy(new))
    json.dump(newdata, out, indent=2)
