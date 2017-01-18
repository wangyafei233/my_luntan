from django.shortcuts import render


# Create your views here.

def freedom_index_view(request, template='freedom/Hotheme Demo.html'):
    return render(request, template)


def freedom_pao_view(request, template='freedom/qipao.html'):
    return render(request, template)
