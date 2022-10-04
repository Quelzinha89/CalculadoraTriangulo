from django.http import HttpResponse, JsonResponse

def home(request, catetoA = '0', catetoB = '0'):
    catetoA_float = float(catetoA)
    catetoB_float = float(catetoB)
    hipotenusa = (catetoA_float ** 2 + catetoB_float ** 2) ** (1/2)
    jsondata = {
        'hipotenusa': '{}'.format(hipotenusa)
    }
    return JsonResponse(jsondata)
