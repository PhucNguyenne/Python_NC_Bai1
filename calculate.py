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
        elif self.method == ":":
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                raise ZeroDivisionError("Cannot divide by zero.")
        else:
            raise ValueError(f"Unknown method {self.method}")

    def TinhBin(self):
        try:
            num1_int = int(str(self.num1), 2)
            num2_int = int(str(self.num2), 2)
        except ValueError:
            raise ValueError("Invalid binary input")

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

    def TinhHex(self):
        try:
            num1_hex = int(str(self.num1), 16)
            num2_hex = int(str(self.num2), 16)
        except ValueError:
            raise ValueError("Invalid hexadecimal input")
        if self.method == "+":
            return hex(num1_hex + num2_hex)[2:].upper()
        elif self.method == "-":
            return hex(num1_hex - num2_hex)[2:].upper()
        elif self.method == "x":
            return hex(num1_hex * num2_hex)[2:].upper()
        elif self.method == ":":
            if num2_hex == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return hex(num1_hex // num2_hex)[2:].upper()
        else:
            raise ValueError(f"Unknown method {self.method}")
