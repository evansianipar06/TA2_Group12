from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "input.html")


def arrses(request):

    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    num3 = int(request.POST['num3'])
    num4 = int(request.POST['num4'])
    num5 = int(request.POST['num5'])
    num6 = int(request.POST['num6'])
    # aktualFeb = int(request.POST['aktualFeb'])

    penjualans = [num1, num2, num3, num4, num5, num6]
    penjualan = [num1, num2, num3, num4, num5, num6, 0]
    peramalan = [0]
    peramalan.append(penjualan[0])
    galat = [0]
    galat_pemulusan = [0]
    galat_absolut = [0]
    alpha = [0]
    beta = 0.6
    alpha.append(beta)
    pe = [0]

    for i in range(1, len(penjualan) - 1):
        galat.append(round(float(penjualan[i] - peramalan[i]), 2))
        peramalan.append(round(float(alpha[i] * penjualan[i]) + (float(1 - alpha[i]) * peramalan[i]), 2))
        galat_pemulusan.append(round(float(beta * galat[i]) + float((1 - beta) * galat_pemulusan[i - 1]), 2))
        galat_absolut.append(round(abs(float(beta * galat[i])) + float((1 - beta) * galat_absolut[i - 1]), 2))
        alpha.append(round(abs(float(galat_pemulusan[i]/1 if galat_absolut[i] == 0 else galat_pemulusan[i]/galat_absolut[i])), 2))
        pe.append(round((abs(float(penjualan[i]/1 if penjualan[i] == 0 else (penjualan[i] - peramalan[i])/penjualan[i]))*100), 2))

    sum_of_pe = round(sum(pe), 2)
    mape = round(sum_of_pe/(len(penjualan)-2), 2)
    accurate_of_forecasting = round(100-mape, 2) 
    jlh_produk = round(peramalan[len(peramalan)-1]) 
    pred = round(peramalan[len(peramalan)-1])
    penjualans.append(pred)


    return render(request, "result.html", {
        "results": accurate_of_forecasting,
        "mape": mape,
        "jlh_produk": jlh_produk,
        "penjualan": penjualan,
        "peramalan": peramalan,
        "penjualans": penjualans,
        "pred" : pred
    })