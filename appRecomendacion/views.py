from django import dispatch
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from appRecomendacion.auth.function_jwt import validate_token, write_token
from appRecomendacion.db.peticiones import buscar_id, busco_relaciones
from appRecomendacion.widgets.filter import ProcesoFiltroDistancia

from appRecomendacion.widgets.scraper import GetRestourantByDestination

import random




geoCordenadas=GetRestourantByDestination()
procesoFiltroDistancia=ProcesoFiltroDistancia()




# Create your views here.
class RecomendationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,requrest):
        try:
            token=requrest.META['HTTP_AUTHORIZATION']
            token=token.replace("Bearer ", "")
            validate_token(token)

            # me aseguro que me envie todos los datos
            try:
                jd=json.loads(requrest.body)

                location=jd['location']
                maxDistance=jd['maxDistance']
                persona=jd['persona']

                # utilizo la clase que me devuelve la lista de restos
                # listOfRestos=geoCordenadas.run("esteban de luca","vegetariano")

                if persona!="":
                    preferences=busco_relaciones(persona)

                    listOfRestos,cor=geoCordenadas.run(location,random.choice(preferences))
                else:
                    listOfRestos,cor=geoCordenadas.run(location,"")
                listaLimpia=procesoFiltroDistancia.ordenoSegunDistancia(listOfRestos['resultados'],cor,float(maxDistance))

                # utilizo la clase que me permite ordenar y filtrar todo
        
                datos={"message":"Succes","restos":listaLimpia}
                return JsonResponse(datos)
            except:
                datos={"result":"Error","message":"Puede haber un parametro mal escrito, de mas o faltar"}
                return JsonResponse(datos)
        except:
            return JsonResponse({"message":"Error","Motive":"token fake"})



class AuthLizy(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,requrest):
        jd=json.loads(requrest.body)
        username=jd['username']
        password=jd['password']


        try:
            passw=buscar_id('avatar','password','email',"'"+username+"'")
            if (password==passw):
                jsonData=write_token(data={
                                "name":username,
                            }
                        )
                return JsonResponse({"message":"Suces","token":jsonData})
            else:
               return JsonResponse({"message":"Error","Motive":"the user or the password ar incorrect"}) 
        except:
            return JsonResponse({"message":"Error","Motive":"the user or the password ar incorrect"})

