class Calculator:        
    def sumar(n1, n2):
        return n1 + n2
    
    def restar(n1, n2):
        return n1 - n2
    
    def multiplicar(n1, n2):
        return n1 * n2
    
    def dividir(n1, n2):
        if (n2 == 0):
            return 'Indeterminado'
        else:
            return n1 / n2
    def num(s):
        try:
            return int(s)
        except ValueError:
            return float(s)