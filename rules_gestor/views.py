#from django.shortcuts import render
#from django.views.decorators.http import require_http_methods 
#from django.http import JsonResponse
#from .gamevariant import get_game_variant

#@require_http_methods(['GET'])
#def get_game_multimedia_by_mode(request):
#    multimedia = get_game_variant(request.GET['mode']).multimedia
#    return JsonResponse(multimedia,safe=False)
