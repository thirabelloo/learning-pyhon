from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos esta incorreta!")


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError("CPF inválido")
    
    def __str__(self) -> str:
        return self.format()

    def valida(self, documento):
        validate_cpf = CPF()
        return validate_cpf.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.documento)

class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError("CNPJ inválido")
    
    def __str__(self) -> str:
        return self.format()

    def valida(self, documento):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)

