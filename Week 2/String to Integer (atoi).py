def myAtoi(self, s: str) -> int:
        string = s.strip()
        is_neg = False
        number_str = ""

        if string:
            if string[0] == "-":
                is_neg = True
                string = string[1:]
            elif string[0] == "+":
                string = string[1:]

        string = string.strip("0")

        for char in string:
            if char.isdigit():
                number_str += char
            else:
                break
        
        number_str = number_str if number_str else "0"
        number = -int(number_str) if is_neg else int(number_str)

        number = -2**31 if number < -2**31 else number
        number = 2**31 - 1 if number > 2**31 - 1 else number

        return number