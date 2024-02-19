class pessoa:
    
    pessoas = []

    def __init__(self, nome, nacimento):
        self._nome = nome.title
        self._nacimento = nacimento 
        self._aniversario = False

    @classmethod
    def __str__(cls):
        for pessoa in cls.pessoas:
            print(f" O nome da pessol é {_nome} o dia do seu nacimento é {_nacimento} e hoje {_aniversario}" )

    @property
    def aniversario():
        return "é aniversario dela" if self.aniversario else "não é aniversario dela"

print(__str__)