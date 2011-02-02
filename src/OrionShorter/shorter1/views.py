# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ValidationError

from models import Map
from OrionShorter.shorter1.utils import geraChave


def home(request):        
    response = render_to_response("base.html",
                                  {
                                   'shorted': ''
                                   }
                                  )
    return response


def short(request):
    retorno = ''
    
    if request.GET.get('target',''):
        param = request.GET.get('target','')
        
        if 'http://localhost:8080/oshtr' in param:
            retorno = "URL já encurtada pelo serviço."
        
        else:    
            pair = Map.objects(url_tgt = param)
            
            if pair.count() > 0:
                #implementar o retorno
                retorno = pair.get().url_sht
                retorno = '<a href=''http://localhost:8080/oshtr/%s''> http://localhost:8080/oshtr/%s </a>' %(str(retorno), str(retorno))
            else:
                try:
                    novo = Map(url_tgt = param)
                    novo.url_sht = geraChave()
                    novo.save()
                    retorno = novo.url_sht
                    retorno = '<a href=''http://localhost:8080/oshtr/%s''> http://localhost:8080/oshtr/%s </a>' %(str(retorno), str(retorno))
                except ValidationError:
                    retorno = "<font color='red'>URL inválida!</font>"
         
    return HttpResponse(retorno)


def get(request):
    param = request.get_full_path()
    param = param.replace("/oshtr/", "")
    
    pair = Map.objects(url_sht = param)
    
    if pair.count() > 0:
        #implementar o retorno
        target = pair.get().url_tgt
        retorno =  HttpResponseRedirect(target)
    else:
        retorno = HttpResponse("Página não encontrada")
        
    return retorno