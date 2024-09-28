class Calculator:
    def __init__(self, num1, num2, method):
        self.num1 = num1
        self.num2 = num2
        self.method = method

    def TinhDec(self):
        if self.method == "+":
            return self.num1 + self.num2
        elif self.method == "-":
            return self.num1 - self.num2
        elif self.method == "x":
            return self.num1 * self.num2
        else:
            if self.num2 != 0:
                return self.num1 / self.num2
            else: 
                pass
    def TinhBin(self):
        num1_str = str(self.num1)
        num1_int = int(num1_str, 2)
        
        num2_str = str(self.num2)
        num2_int = int(num2_str, 2)
        
        if self.method == "AND":
            return bin(num1_int & num2_int)[2:] 
        elif self.method == "XOR":
            return bin(num1_int ^ num2_int)[2:]  
        elif self.method == "OR":
            return bin(num1_int | num2_int)[2:] 
        elif self.method == "=":
            return num1_int == num2_int
        else:
            raise ValueError("Unknown binary operation")

