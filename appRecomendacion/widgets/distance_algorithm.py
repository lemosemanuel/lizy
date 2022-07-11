from math import cos, asin, sqrt


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest(data, v):

    return min(data, key=lambda p: distance(float(v['lat']),float(v['lon']),float(p['lat']),float(p['long'])))



# tempDataList = [
#         {
#             "id": 1,
#             "name": "Distrito Restó",
#             "calification": "4,0",
#             "lat": "-34.6347928",
#             "long": "-58.405778000000005",
#             "distance": 0.40754767094863864
#         },
#         {
#             "id": 2,
#             "name": "La Vaca Atada",
#             "calification": "4,2",
#             "lat": "-34.6328932",
#             "long": "-58.39574759999999",
#             "distance": 0.6970378196634736
#         },
#         {
#             "id": 4,
#             "name": "Parrilla Los Nenes",
#             "calification": "4,0",
#             "lat": "-34.638049599999995",
#             "long": "-58.397882",
#             "distance": 0.8525961658049638
#         },
#         {
#             "id": 5,
#             "name": "Muzarella",
#             "calification": "4,1",
#             "lat": "-34.636494899999995",
#             "long": "-58.4033059",
#             "distance": 0.5244027021090277
#         },
#         {
#             "id": 6,
#             "name": "Aloha",
#             "calification": "4,2",
#             "lat": "-34.633981299999995",
#             "long": "-58.4109601",
#             "distance": 0.7475193476717545
#         },
#         {
#             "id": 7,
#             "name": "La Taberna de Roberto",
#             "calification": "4,1",
#             "lat": "-34.635226599999996",
#             "long": "-58.410319599999994",
#             "distance": 0.752600436433765
#         },
#         {
#             "id": 8,
#             "name": "El codo",
#             "calification": "4,1",
#             "lat": "-34.6372585",
#             "long": "-58.408741899999995",
#             "distance": 0.7902829396785657
#         },
#         {
#             "id": 9,
#             "name": "El Barcito",
#             "calification": "4,4",
#             "lat": "-34.6345284",
#             "long": "-58.409298500000006",
#             "distance": 0.6329191312382911
#         },
#         {
#             "id": 11,
#             "name": "Il Ombu Trattoria Italiana",
#             "calification": "4,8",
#             "lat": "-34.6385223",
#             "long": "-58.404796",
#             "distance": 0.7632335996743329
#         },
#         {
#             "id": 12,
#             "name": "Bar de Sabores de Parque Patricios",
#             "calification": "4,0",
#             "lat": "-34.636897999999995",
#             "long": "-58.40547300000001",
#             "distance": 0.6046986894328015
#         },
#         {
#             "id": 13,
#             "name": "Las Familias",
#             "calification": "4,1",
#             "lat": "-34.6366583",
#             "long": "-58.402228199999996",
#             "distance": 0.5504329142946666
#         },
#         {
#             "id": 14,
#             "name": "Los Camioneros",
#             "calification": "4,2",
#             "lat": "-34.6374183",
#             "long": "-58.4001751",
#             "distance": 0.6870568851581315
#         },
#         {
#             "id": 15,
#             "name": "American Burger parque patricios",
#             "calification": "4,4",
#             "lat": "-34.639406699999995",
#             "long": "-58.40459399999999",
#             "distance": 0.857217381969346
#         },
#         {
#             "id": 16,
#             "name": "Restaurante El Refugio",
#             "calification": "4,5",
#             "lat": "-34.6342442",
#             "long": "-58.395044299999995",
#             "distance": 0.7987977494586629
#         },
#         {
#             "id": 19,
#             "name": "Pizzería El Globito",
#             "calification": "4,2",
#             "lat": "-34.6370125",
#             "long": "-58.4058859",
#             "distance": 0.6302187282372416
#         },
#         {
#             "id": 20,
#             "name": "Mercado de las Ranas",
#             "calification": "4,9",
#             "lat": "-34.6361388",
#             "long": "-58.40232770000001",
#             "distance": 0.49194162415902726
#         }
#     ]

# v = {'lat': -34.637121, 'lon': -58.405647}

# print(closest(tempDataList, v))


