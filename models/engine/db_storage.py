#!/usr/bin/python3
"""
Module that connects to the database
"""
import hashlib
from models.base_model import BaseModel
from models.user import User
import MySQLdb
import MySQLdb.cursors


class DBStorage():
    """
    Class that interacts with
    the MySQL database
    """
    def __init__(self):
        """
        Method that initializes the
        connection to the database
        """
        self.db = MySQLdb.connect(user='root', passwd='1999151',
                                  db='gbs_dev_db', host='localhost',
                                  port=3306,
                                  cursorclass=MySQLdb.cursors.DictCursor)

        self.cursor = self.db.cursor()

    def all(self, tablename=None):
        """
        Method that consults in the current session
        of the database and returns all the data
        of the indicated table
        """
        dict_result = {}

        query = "SELECT * FROM {} ORDER BY id DESC;".format(tablename)
        self.cursor.execute(query)
        tupla = self.cursor.fetchall()

        for dictionary in tupla:
            key = tablename + '.' + str(dictionary['id'])
            dict_result[key] = dictionary

        return dict_result

    def create(self, dic, procedure):
        """
        Method that adds values to the
        indicated table of the current session
        """
        lis = []

        for values in dic.values():
            lis.append(values)

        self.cursor.callproc(procedure, lis)
        self.db.commit()

    def get(self, tablename, id):
        """
        Method that obtains and returns the values
        of a single object of the current session
        """
        if tablename is not None or id is not None:
            query = self.all(tablename).values()

            for values in query:
                if values['id'] == id:
                    return values
        return None

    def to_dict(self, cls_name=None, dic={}):
        """
        Method that returns a dictionary
        to be displayed in the APIs
        """
        dic["__class__"] = cls_name

        if "password" in dic:
            del dic["password"]

        return dic

    def update(self, dic, id, procedure):
        """
        Method that receives a dictionary from
        the api and an id, to update its indicated data
        """
        lis = []
        lis.append(id)

        black_list = ["id", "created_at", "updated_at"]

        for ignore in black_list:
            if ignore in dic:
                del dic[ignore]

        if "password" in dic:
            encrypt_pwd = hashlib.md5(dic['password'].encode())
            dic['password'] = encrypt_pwd.hexdigest()

        for values in dic.values():
            lis.append(values)

        self.cursor.callproc(procedure, lis)
        self.db.commit()

    def verify(self, tablename, email, id=None):
        """
        Method that checks if an
        email is in the database
        """
        if id is None:
            query = "SELECT * FROM {} WHERE email='{}'".format(tablename,
                                                               email)
        else:
            query = "SELECT * FROM {} WHERE email='{}'\
                     AND id!={}".format(tablename, email, id)

        self.cursor.execute(query)
        tupla = self.cursor.fetchall()
        for dictionary in tupla:
            return dictionary

    def delete(self, tablename, id):
        """
        Method that receives the name of the
        table and the id of the data that I want
        to delete from the database
        """
        self.cursor.execute("DELETE FROM {} WHERE id={};".format(tablename,
                                                                 id))
        self.db.commit()

    def count(self):
        """
        Method that returns a dictionary with all
        the tables and the number of their records
        """
        str_1 = "SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES"
        query = str_1 + " WHERE TABLE_SCHEMA = 'gbs_dev_db'"

        self.cursor.execute(query)
        tupla = self.cursor.fetchall()

        dict_result = {}
        for dictionary in tupla:
            values = list(dictionary.values())
            dict_result[values[0]] = values[1]

        return dict_result

    def filters(self, tablename, filtro, value):
        """
        Method that filters any table with Where
        """
        if not tablename or not filtro or not value:
            return None

        list_result = []

        str_1 = "SELECT * FROM {} WHERE".format(tablename)
        query = str_1 + " {}={} ORDER BY id DESC;".format(filtro, value)

        self.cursor.execute(query)
        tupla = self.cursor.fetchall()

        for dictionary in tupla:
            list_result.append(dictionary)

        return list_result

    # -------------------INI-GERARDO-CARGA MASIVA-HELPER---------------------
    def create_many(self, data=[], carga=None):
        """
        Method that allows further insertion through the user and income tables
        """
        if carga == 'usuarios':
            sql = "INSERT INTO user (first_name,last_name,id_document_type,\
                   number_document,email,password,phone,birth_date,id_role) \
                   VALUE (%s,%s,%s,%s,%s,MD5(%s),%s,%s,%s)"

            self.cursor.executemany(sql, data)
        elif carga == 'ingresos':
            sql = "insert into income (nro_recibo,id_user,id_departament, \
                   id_type_payment,dia,mes,a??o,numero_operacion,banco, \
                   lugar_pago,modalidad,id_concepto,a??o_concepto,import) \
                   values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.executemany(sql, data)
        self.db.commit()

    def get_id(self, table=None, atributo=None, name=None):
        """
        Method to obtain the id according to the attribute searched for
        by fixed word
        """
        self.cursor.execute("SELECT id, {} FROM {} where {} \
            LIKE %(name)s".format(atributo, table, atributo), {
            'name': name
        })
        row = self.cursor.fetchall()
        for dictionary in row:
            return dictionary.get('id')

    # -------------------FIN-GERARDO-CARGA MASIVA-HELPER---------------------
