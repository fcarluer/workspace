class Calculator(object):
 
    def add(self, x, y):
        number_types = (int,  float, complex)
        
        if isinstance(x, number_types) and isinstance(y,number_types):
            result = x + y
            return result
        else:
            raise ValueError
        
    def soustract(self, x, y):
        number_types = (int,  float, complex)
        
        if isinstance(x, number_types) and isinstance(y,number_types):
            result = x - y
            return result
        else:
            raise ValueError
        
    def divide(self, x, y):
        number_types = (int,  float, complex)
        
        if isinstance(x, number_types) and isinstance(y,number_types):
            result = x / y
            return result
        else:
            raise ValueError       
    
    def multiply(self, x, y):
        number_types = (int,  float, complex)
        
        if isinstance(x, number_types) and isinstance(y,number_types):
            result = x * y
            return result
        else:
            raise ValueError   