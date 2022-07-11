from appRecomendacion.db.conection import connectDB


def crearTabla(tableName,columnasInString):
    try:
        con, cursor = connectDB()
        sql =""" CREATE TABLE """+tableName+""" ( id SERIAL PRIMARY KEY, """+columnasInString+""" )"""
        cursor.execute(sql)
        con.commit()
        con.close()
        print('Tabla creada con exito')
    except:
        print('No se pudo crear la tabla')

    return sql




crearTabla('avatar','''
                    name varchar(20) not null,
                    email varchar(20) not null,
                    password varchar(20) not null
            ''')

crearTabla('food_type','''
                    name varchar(20) not null
            ''')

crearTabla('avart_food_type','''
                                avatar_id int not null,
                                food_type_id int not null,
                                foreign key (avatar_id) references avatar(id),
                                foreign key (food_type_id) references food_type(id)
            ''')       


def insertData(tabla,columns,values):
    try:
        con, cursor = connectDB()
        if '(' in values:
            sql =""" INSERT INTO """+tabla+""" ("""+columns+""") VALUES """+values+""" ;"""
        else:
            sql =""" INSERT INTO """+tabla+""" ("""+columns+""") VALUES ("""+values+""") ;"""
        cursor.execute(sql)
        con.commit()
        con.close()
        print('Tabla creada con exito')
    except:
        print('No se pudo crear la tabla')

    return sql




insertData(
        'avatar',
        """
            name,
            email,
            password
        """,
            """
        ('Gilles','gilles@gmail.com','123123'),
        ('Gaelle','Gaelle@gmail.com','123123'),
        ('Vince','Vince@gmail.com','123123'),
        ('Sam','Sam@gmail.com','123123'),
        ('Klaas','Klaas@gmail.com','123123')
        """
        )

insertData(
        'food_type',
        """
            name
        """,
            """
        ('Italian'),
        ('Lebanese'),
        ('Japanese'),
        ('Belgian')
        """
        )


insertData(
        'avatar_food_type',
        """
            avatar_id,
            food_type
        """,
            """
        ('2','3'),
        ('2','2'),
        ('5','4'),
        ('5','3'),
        ('4','4'),
        ('3','2'),
        ('3','1'),
        ('3','3'),
        ('1','1'),
        ('1','2'),
        ('1','3'),
        ('1','4'),
        """
        )