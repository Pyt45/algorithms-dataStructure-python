from __future__ import annotations

class Converter:
    def __init__(self, con: str | int) -> None:
        self.con = con
    # def convert_to_str(self) -> str:
    #     if isinstance(self.con, int):


    def convert_to_str(self) -> int:
        if isinstance(self.con, int):
            def num_len():
                i = 0
                n = self.con * -1 if self.con < 0 else self.con
                while n:
                    i += 1
                    n //= 10
                return i
            res = ''
            if self.con < 0:
                res += '-'
            num = self.con * -1 if self.con < 0 else self.con
            for i in range(num_len()):
                res += str((num // ( 10 ** (num_len() - i - 1) )))
                num -= (num // (10 ** (num_len() - i - 1))) * (10 ** (num_len() - i - 1))
            return res
        return None

if __name__ == '__main__':
    s = Converter(-12345)
    # n = Converter(12345)
    print(s.convert_to_str())
    # print(n.convert_to_str())