
# calculated the distance of each one based on a point
from math import sin , cos , sqrt, atan2, radians
from appRecomendacion.widgets.distance_algorithm import *

class ProcesoFiltroDistancia:
    def calculoDistancia(self,jsonPython,imHere):
        # radio de la tierra
        for i in range(len(jsonPython)):
            R = 6373.0
            lat1=radians(float(imHere['lat']))
            lon1=radians(float(imHere['lon']))
            lat2=radians(float(jsonPython[i]['lat']))
            lon2=radians(float(jsonPython[i]['long']))

            dlon=lon2-lon1 
            dlat=lat2-lat1 

            a = sin(dlat/2)**2 +cos(lat1)*cos(lat2)*sin(dlon/2)**2
            c= 2*atan2(sqrt(a),sqrt(1-a))

            distancia=R*c
            jsonPython[i]['distance']=distancia
            listaConDistancias=jsonPython
        return listaConDistancias

    # filter those that have less distance than the established one
    def filtroPorMetros(self,metros,jsonPython,imHere):
        dataAgregoDistancia=self.calculoDistancia(jsonPython,imHere)
        listaAprovados=[]
        for i in dataAgregoDistancia:
            if i['distance']<metros:
                listaAprovados.append(i)
            else:
                pass
        return listaAprovados


    def ordenoSegunDistancia(self,jsonPython,imHere,metros):
        coordenadasDadas=imHere
        jsonPythonFiltrado=self.filtroPorMetros(metros,jsonPython,imHere)
        listaReduccion=jsonPythonFiltrado
        odenadoByNear=[]
        contador=0

        for i in range(len(listaReduccion)):
            contador+=1
            near=closest(jsonPythonFiltrado, coordenadasDadas)
            listaReduccion.remove(near)
            len(listaReduccion)
            near['id']=contador
            odenadoByNear.append(near)
        return odenadoByNear    