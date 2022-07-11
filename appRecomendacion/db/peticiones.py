import psycopg2
from appRecomendacion.db.conection import connectDB



def buscar_id(tabla,columnaAdevolver,column,valor):
    try:
        con, cursor = connectDB()
        if type(valor) is tuple:
            sql =""" SELECT """+tabla+'.'+columnaAdevolver+""" FROM """+tabla+""" WHERE """+column+""" in """+str(valor)+""" """       
        else:
            # print('no es tupla')
            sql =""" SELECT """+tabla+'.'+columnaAdevolver+""" FROM """+tabla+""" WHERE """+column+""" in ("""+valor+""") """    
        cursor.execute(sql)
        lista=()
        for x in cursor:
            lista+=x
        # con.commit()
        # con.close()
        print('se encontro el dato')
        if len(lista)==1:
            return lista[0]
        else:
            return lista
    except:
        print('No se encontro el dato')



def busco_relaciones(name):
    # looking for person
    idAvatar=buscar_id('avatar','id','name',"'"+name+"'")
    # look for food id
    idFood=buscar_id('avatar_food_type','food_type','avatar_id',str(idAvatar))
    # find food name 
    foodName=buscar_id('food_type','name','id',idFood)

    return foodName

