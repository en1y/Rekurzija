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
            for i in range(domino_num):
                self.free_domino_list.append(self.domino_generator())
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
        while True:
            num1 = secrets.choice(range(7))
            num2 = secrets.choice(range(7))
            if Dominoes(num1, num2) not in self.free_domino_list:
                return Dominoes(num1, num2)

    # def create_chain(self, free_dominoes_num, start=0, finish=0, possibility_num=0):
    #     for i in range(free_dominoes_num):
    #         base_domino = self.free_domino_list[i]
    #         if finish == 0:
    #             self.domino_chain.append([base_domino])
    #             self.free_domino_list.pop(i)
    #             self.create_chain(free_dominoes_num - 1, base_domino.first_num, base_domino.second_num, possibility_num)
    #             self.free_domino_list.insert(0, base_domino)
    #             possibility_num += 1
    #         elif len(self.domino_chain[possibility_num]) == self.dominoes_num:
    #             continue
    #         else:
    #             start = self.domino_chain[possibility_num][0].first_num
    #             finish = self.domino_chain[possibility_num][len(self.domino_chain[possibility_num]) - 1].second_num
    #             start_finish_domino = Dominoes(start, finish)
    #             if base_domino.connectable(start_finish_domino):
    #                 if base_domino.connectable_left(finish):
    #                     self.domino_chain[possibility_num].append(base_domino)
    #                     self.free_domino_list.pop(i)
    #                     self.create_chain(free_dominoes_num - 1, start, base_domino.second_num, possibility_num)
    #                     self.free_domino_list.insert(0, base_domino)
    #                 elif base_domino.connectable_right(finish):
    #                     base_domino = base_domino.reverse()
    #                     self.domino_chain[possibility_num].append(base_domino)
    #                     self.free_domino_list.pop(i)
    #                     self.create_chain(free_dominoes_num - 1, start, base_domino.second_num, possibility_num)
    #                     self.free_domino_list.insert(0, base_domino.reverse())
    #                 elif base_domino.connectable_right(start):
    #                     self.domino_chain[possibility_num].insert(0, base_domino)
    #                     self.free_domino_list.pop(i)
    #                     self.create_chain(free_dominoes_num - 1, base_domino.first_num, finish, possibility_num)
    #                     self.free_domino_list.insert(0, base_domino)
    #                 else:
    #                     base_domino = base_domino.reverse()
    #                     self.domino_chain[possibility_num].insert(0, base_domino)
    #                     self.free_domino_list.pop(i)
    #                     self.create_chain(free_dominoes_num - 1, base_domino.first_num, finish, possibility_num)
    #                     self.free_domino_list.insert(0, base_domino.reverse())
    def create_chain(self, free_dominoes_num = -1, start=0, finish=0):
        changed = False
        # "B" - base orientation, "R" - reversed orientation
        for i in range(free_dominoes_num):
            base_domino = self.free_domino_list[i]
            self.free_domino_list.pop(i)
            if start == 0:
                start = base_domino.first_num
                finish = base_domino.second_num
                self.domino_chain.append([Dominoes(start, finish), 'B'])
                self.create_chain(free_dominoes_num - 1, start, finish,)
                self.free_domino_list.insert(i, base_domino)
                self.domino_chain.pop(0)
                start = 0
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
            return (self.maxPath, self.maxL)


def main():
    domino_num = int(input("Enter domino number:\n"))
    domino_chain = DominoChain(domino_num)
    domino_chain.create_chain(len(domino_chain.free_domino_list))
    print(domino_chain)



main()
