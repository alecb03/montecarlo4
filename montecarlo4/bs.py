"""test"""     

import numpy as np
class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        """Constructor

        Parameters
        ----------
        N: Number of bits in bit string

        Self: Refers to the object 
        """
        self.N = N
        self.config = np.zeros(N, dtype=int) 
        

    def __str__(self):
        """String Method

        Parameters
        ----------
        Self: Refers to the object 
        """
        return str(self.config)

    def __repr__(self):
        """Representation Method
        
        Parameters
        ----------
        Self: Refers to the object 
        """
        return f"Bitstring((self.config.tolist))"

    def __eq__(self, other):  
        """Equality Mathod
        
        Parameters
        ----------
        Self: Refers to the object 

        Other: Referse to another bitsting
        """      
        return np.array_equal(self.config, other.config)

    
    def __len__(self):
        """Length Method
        
        Parameters
        ----------
        Self: Refers to the object 
        """
        return len(self.config)


    def on(self):
        """On Method 
        Gives how many bits are on

        Parameters
        ----------
        Self: Refers to the object 
        """
        count = 0
        for i in range(len(self.config)):
            if self.config[i] == 1:
                count += 1
        return count
    
    def off(self):
        """Off Method 
        Gives how many bits are off

        Parameters
        ----------
        Self: Refers to the object 
        """
        count = 0
        for i in range(len(self.config)):
            if self.config[i] == 0:
                count += 1
        return count
    
    def flip_site(self,i):
        """Flip Site method
        Flips the values of each bit

        Parameters
        ----------
        Self: Refers to the object 

        i: Refers to an index of the bits
        """
        self.config[i] = 1 - self.config[i]
        
    
    def int(self):
        """Integer Function
        Converts the bitstring into a decimal
        
        Parameters
        ----------
        Self: Refers to the object
        """
        dec = 0
        power = len(self.config) - 1  
        for i in self.config:
            dec = dec + i *(2**power) 
            power = power - 1
        return dec

 

    def set_config(self, s:list[int]):
        """Set Config Method
        Converts bitstring into a list
        Parameters
        ----------
        Self: Refers to the object

        S: a list
        """
        self.config = list(s)
        
    def set_int_config(self, dec: int):
        """Set Integer Config Method
        Converts an integer into a bitsting
        Parameters
        ----------
        Self: Refers to the object

        dec: an integer
        """
        for i in range(-1, -self.N - 1, -1):
            curr_bit = dec % 2
            self.config[i] = curr_bit
            dec = dec // 2
        return self
