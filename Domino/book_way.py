import secrets


class Dominoes:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __repr__(self):
        return f"({self.first_num}, {self.second_num})"

    def __copy__(self):
        return Dominoes(self.first_num, self.second_num)

    def __eq__(self, other):
        if type(other) == Dominoes:
            if self.first_num == other.first_num and self.second_num == other.second_num:
                return True
            return False
        raise TypeError("Dominoes may be only compared to Dominoes")

    def connectable(self, not_self):
        """Callable with Dominoes item type"""
        if type(not_self) == Dominoes:
            if self.first_num == not_self.first_num or self.first_num == not_self.second_num or self.second_num == not_self.first_num or self.second_num == not_self.second_num:
                return True
            return False
        raise TypeError("Only callable with Dominoes item type")

    def connectable_left(self, num):
        if type(num) == int:
            if self.first_num == num:
                return True
            return False
        raise TypeError("Only callable with int item type")

    def connectable_right(self, num):
        if type(num) == int:
            if self.second_num == num:
                return True
            return False
        raise TypeError("Only callable with int item type")

    def reverse(self):
        domino = self.__copy__()
        second_num_buffer = domino.second_num
        domino.second_num = domino.first_num
        domino.first_num = second_num_buffer
        return domino


class DominoChain:
    def __init__(self, domino_num):
        if domino_num > 28:
            domino_num = 28
        self.free_domino_list = []
        gen_or_input = input("""Write generate if you want automatically generated dominoes or write input if you want to input dominoes yourself\n""")
        if gen_or_input.lower().startswith("input"[:len(gen_or_input)]):
            for i in range(domino_num):
                inp = [int(j) for j in input().split()]
                if len(inp) == 2 and 0 <= inp[0] <= 6 and 0 <= inp[1] <= 6:
                    self.free_domino_list.append(Dominoes(inp[0], inp[1]))
                else:
                    raise TypeError("You have to input 2 elements both of which are in between 1 and 6")
        elif gen_or_input.lower().startswith("generate"[:len(gen_or_input)]):
            self.domino_generator()
            print(f"These are the the generated dominoes: {[i for i in self.free_domino_list]}")
        else:
            raise Exception("You have to write generate or input")
        self.domino_chain = []
        self.dominoes_num = domino_num
        self.maxL = 0
        self.maxPath = []

    def __repr__(self):
        result = """"""
        for i in self.maxPath:
            if i[1] == 'B':
                result += f"{i[0]} "
            elif i[1] == 'R':
                result += f"{i[0].reverse()} "
        result += f"\nMax length is {self.maxL}"
        return result

    def domino_generator(self):
        for i in range(7):
            for j in range(7):
                self.free_domino_list.append(Dominoes(i, j))
        for i in range(28 - self.dominoes_num):
            delete_num = secrets.choice(range(self.dominoes_num))
            self.free_domino_list.pop(delete_num)

    def create_chain(self, free_dominoes_num=-1, start=0, finish=0):
        changed = False
        # "B" - base orientation, "R" - reversed orientation
        for i in range(free_dominoes_num):
            base_domino = self.free_domino_list[i]
            self.free_domino_list.pop(i)
            if start == 0:
                finish = base_domino.second_num
                self.domino_chain.append(base_domino, 'B'])
                self.create_chain(free_dominoes_num - 1, base_domino.first_num, finish,)
                self.free_domino_list.insert(i, base_domino)
                self.domino_chain.pop(0)
            else:
                if finish == base_domino.first_num:
                    self.domino_chain.append([base_domino, 'B'])
                    self.create_chain(free_dominoes_num - 1, start, base_domino.second_num)
                    changed = True
                elif finish == base_domino.second_num:
                    self.domino_chain.append([base_domino, 'R'])
                    self.create_chain(free_dominoes_num - 1, start, base_domino.first_num)
                    changed = True
                else:
                    self.free_domino_list.insert(i, base_domino)
            if (len(self.domino_chain) > self.maxL) or (len(self.domino_chain) == self.dominoes_num):
                self.maxL = len(self.domino_chain)
                self.maxPath = self.domino_chain.copy()
            if changed and self.domino_chain[len(self.domino_chain) - 1][0] == base_domino:
                self.free_domino_list.insert(i, self.domino_chain[len(self.domino_chain) - 1][0])
                self.domino_chain.pop(len(self.domino_chain) - 1)
        if (start == 0 and finish != 0 and free_dominoes_num == 0) or (self.maxL == self.dominoes_num):
            return self.maxPath, self.maxL


def main():
    domino_num = int(input("Enter domino number:\n"))
    domino_chain = DominoChain(domino_num)
    domino_chain.create_chain(len(domino_chain.free_domino_list))
    print(domino_chain)


main()
