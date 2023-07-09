class BaseFunctions():
    def to_json(objeto):
        objeto = objeto.__dict__
        indesejado = [*objeto.keys( )][0]
        objeto.pop(indesejado)
        return objeto
    
