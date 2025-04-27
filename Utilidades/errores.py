class Errores(Exception):
    pass

class ErrorNoEsNumero(Errores):
    def __init__(self, mensaje, codigo_error):
        super().__init__(mensaje)
        self.codigo_error = codigo_error
        
class ErrorNumeroInvalido(Errores):
    def __init__(self, mensaje, codigo_error):
        super().__init__(mensaje)
        self.codigo_error = codigo_error
        
class ErrorCarritoVacio(Errores):
    def __init__(self, mensaje, codigo_error):
        super().__init__(mensaje)
        self.codigo_error = codigo_error
        
class ErrorProductoNoEncontrado(Errores):
    def __init__(self, mensaje, codigo_error):
        super().__init__(mensaje)
        self.codigo_error = codigo_error