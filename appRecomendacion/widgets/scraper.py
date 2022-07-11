from email import header
import json
from appRecomendacion.env.settings import *
import requests
from bs4 import BeautifulSoup


# GeoCoordenates
class GetRestourantByDestination():
    urlForFindLocation=Settings.urlForFindLocation
    urlForFindRestos=Settings.urlForFindRestos
    params=Settings.params
    headers=Settings.headers

    # here only make the request, depending on whether I want to find the place, or (if I already have it), find nearby restaurants
    def fetch(self,query,motive):
        if motive=="FindLocation":
            self.params['q']=query
            return requests.get(self.urlForFindLocation,params=self.params,headers=self.headers)
        else:
            self.params['q']="restaurants "+ str(query)
            return requests.get(self.urlForFindRestos,params=self.params,headers=self.headers)

    # Find Place Coordinates
    def locateCoordenates(self,html):
        data={'resultados':[]}
        content = BeautifulSoup(html.text, 'lxml')
        content.find_all('div',{'class':'DviQ8b'})
        tags = content.find_all('div',{'class':'DviQ8b'})[0].a['href']
        coordenates=tags.split('@')[1].split(',')[:2]
        lat=coordenates[0]
        log=coordenates[1]
        return lat, log
    
    # locate the city in case they send me coordinates
    def locateCity(self,lat,log):
        response=requests.get('https://api.opencagedata.com/geocode/v1/json?q='+lat+'+'+log+'&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en',headers=self.headers)
        content=response.content.decode('utf8')
        lugar = json.loads(content)['results'][0]['formatted']
        return lugar

    # I need a function that defines how the location data comes
    def esCoordenadas(self,input):
        try:
            for i in input.split(','):
                float(i)
            print('Son coordenadas')
            return True
        except:
            print('Son datos especificos')
            return False

    # returns a list of restaurants based on location
    def listOfRestaurantByLocation(self,html):
        data={'resultados':[]}
        content = BeautifulSoup(html, 'lxml')
        title=[title.text for title in content.findAll("div",{"class":"vzRMeAg4Oi8__kl-trunc-name"})]
        calificacion=[calificacion.text for calificacion in content.findAll("span",{"class":"YDIN4c YrbPuc"})]
        lat=[]
        long=[]
        price=[]
        for i in range(len(title)):
            lat.append(str(content.findAll("div",{"class":"rllt__mi"})[i]['data-lat']))
            long.append(str(content.findAll("div",{"class":"rllt__mi"})[i]['data-lng']))


        #build json
        for i in range(len(title)):
            data['resultados'].append({
                'id':i+1,
                'name':title[i],
                'calification':calificacion[i],
                'lat':lat[i],
                'long':long[i]
            })
        return data



    #run code
    def run(self,location,description=""):
        esCoordenadas=self.esCoordenadas(location)
        if esCoordenadas ==False:
            response=self.fetch(location,'FindLocation')
            if response.status_code == 200:   
                # find coordinates
                lat,lon=self.locateCoordenates(response)
                coordenadas={}
                coordenadas['lat']=lat
                coordenadas['lon']=lon
                #  correct the place, look for the neighborhood to cover more restaurants
                locateCity=self.locateCity(coordenadas['lat'],coordenadas['lon'])

                # look restos
                fechResto=self.fetch(locateCity.split(',')[1]+" "+locateCity.split(',')[1]+" "+description,'FindResto')
                listOfRestos= self.listOfRestaurantByLocation(fechResto.text)

            else:
                print('hubo un error en la peticion')

        else: # in case of be coordinates
            coordenadas={}
            coordenadas['lat']=location.split(',')[0]
            coordenadas['lon']=location.split(',')[1]
            locateCity=self.locateCity(coordenadas['lat'],coordenadas['lon'])
            fechResto=self.fetch(locateCity.split(',')[1]+" "+description,'FindResto')            
            listOfRestos= self.listOfRestaurantByLocation(fechResto.text)
        
        return listOfRestos, coordenadas
