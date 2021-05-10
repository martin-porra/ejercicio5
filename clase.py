class estudiante:
    __cantidad_maxima_ina = 10
    __cant__Clases = 8

    def __init__(self, nombre, año, division, inasis):
        self.__nombre = nombre
        self.__año = año
        self.__division = division
        self.__inasistencia = inasis

    def nombre(self):
        return self.__nombre
    def año(self):
     return self.__año
    def division(self):
      return  self.__division
    def inas(self):
        return self.__inasistencia
    def porcentaje(self):
      porce = (int(self.__inasistencia) * 100) / int(self.__cantidad_maxima_ina)
      return porce
    @classmethod
    def max(cls):
     return cls.__cantidad_maxima_ina
    @classmethod
    def modi(cls, b):
      cls.__cantidad_maxima_ina = b
