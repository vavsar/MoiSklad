import json
import copy

with open('Заказы.json', encoding="utf8") as dataf, open('data2.json',
                                                          'w') as out:
    data = json.load(dataf)
    newdata = []
    for i, block in enumerate(data):
        new = dict(model="wares.order", pk=i + 1)
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
            warehouseName=block['warehouseName'],
            oblast=block['oblast'],
            incomeID=block['incomeID'],
            odid=block['odid'],
            nmId=block['nmId'],
            subject=block['subject'],
            category=block['category'],
            brand=block['brand'],
            isCancel=block['isCancel'],
            cancel_dt=block['cancel_dt'],
            gNumber=block['gNumber'],
        )
        newdata.append(copy.deepcopy(new))
    json.dump(newdata, out, indent=2)
