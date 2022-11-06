class Aluno:
   
   def __init__(self, nomeCompleto: str, matricula: int, email: str, senha:str):
      self.__nomeCompleto = nomeCompleto
      self.__matricula = matricula
      self.__email = email
      self.__senha = senha
   
   @property
   def nomeCompleto(self):
      return self.__nomeCompleto

   @nomeCompleto.setter
   def nomeCompleto(self, nomeCompleto: str):
      self.__nome = nomeCompleto

   @property
   def matricula(self):
      return self.__matricula

   @matricula.setter
   def matricula(self, matricula):
      self.__matricula = matricula

   @property
   def email(self):
      return self.__email

   @email.setter
   def email(self, email):
      self.__email = email

   @property
   def senha(self):
      return self.__senha
   
   @senha.setter
   def senha(self, senha):
      self.__senha = senha