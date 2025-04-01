class Pessoa:
    def __init__(self, nome, idade, ):
        self.nome = nome
        self.idade = idade



class Student(Pessoa):
    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(nome, idade,matricula)
        self.matricula = matricula
        
    def display_information(self):
        print(f'Name: {self.nome} Age: {self.idade} matricula: {self.matricula}')
        
        
aluno1 = Student('gabriel','12', '123233')
aluno1.display_information()
