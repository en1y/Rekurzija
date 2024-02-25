class Dominoes:
    dominoes_num = 0

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num
        Dominoes.dominoes_num += 1
        self.id = Dominoes.dominoes_num

    def __repr__(self):
        return f"({self.first_num}, {self.second_num})"

    def __copy__(self):
        return Dominoes(self.first_num, self.second_num)

    def __eq__(self, other):
        if type(other) == Dominoes:
            if self.id == other.id:
                return True
            return False
        raise TypeError("Dominoes may be only compared to Dominoes")

    def alike(self, other):
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
        second_num_buffer = self.second_num
        self.second_num = self.first_num
        self.first_num = second_num_buffer

    def reverse_copy(self):
        domino = self.__copy__()
        second_num_buffer = domino.second_num
        domino.second_num = domino.first_num
        domino.first_num = second_num_buffer
        return domino


class DominoChain:
    def __init__(self, domino_num):
        domino_list = []
        for i in range(domino_num):
            inp = [int(j) for j in input().split()]
            if len(inp) == 2 and 0 < inp[0] <= 6 and 0 < inp[1] <= 6:
                domino_list.append(Dominoes(inp[0], inp[1]))
            else:
                raise TypeError("You have to input 2 elements both of which are in between 1 and 6")
        self.free_domino_list = domino_list.copy()
        self.domino_chain = []
        self.dominoes_num = len(self.free_domino_list)
        self.all_possibilities = []
        self.max_len = 0
        self.current_len = 0

    def __repr__(self):
        # self.update()
        result = """"""
        for i in self.all_possibilities:
            result += f"{i} \n"
        return result

    def update(self):
        res = []
        [res.append(x) for x in self.all_possibilities if x not in res]
        self.all_possibilities = res.copy()

    def create_chain(self, free_dominoes_num=-1, start=0, finish=0):
        if free_dominoes_num == -1:
            free_dominoes_num = self.dominoes_num
        for i in range(free_dominoes_num):
            base_domino = self.free_domino_list[i]
            if finish == 0:
                start = base_domino.first_num
                finish = base_domino.second_num
                self.current_len = 1
                self.domino_chain.append(base_domino)
                self.all_possibilities.append([base_domino])
                self.free_domino_list.pop(i)
                self.create_chain(free_dominoes_num-1, start, finish)
                finish = 0
                self.domino_chain.pop(0)
                self.free_domino_list.insert(0, base_domino)
                if self.max_len < self.current_len:
                    self.max_len = self.current_len
            elif base_domino not in self.all_possibilities[len(self.all_possibilities) - 1]:
                start_finish_domino = Dominoes(self.all_possibilities[len(self.all_possibilities) - 1][0].first_num,
                                               self.all_possibilities[len(self.all_possibilities) - 1][len(self.all_possibilities[len(self.all_possibilities) - 1]) - 1].second_num)
                # start_finish_domino = Dominoes(start, finish)
                if base_domino.connectable(start_finish_domino):
                    if base_domino.connectable_left(finish):
                        self.domino_chain.append(base_domino)
                        self.all_possibilities[len(self.all_possibilities) - 1].append(base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, start, base_domino.second_num)
                        self.all_possibilities.append(self.all_possibilities[len(self.all_possibilities) - 1].pop(self.domino_chain[len(self.domino_chain) - 1]))
                        self.domino_chain.pop(len(self.domino_chain) - 1)
                        self.free_domino_list.insert(0, base_domino)
                    elif base_domino.connectable_right(finish):
                        base_domino.reverse()
                        self.domino_chain.append(base_domino)
                        self.all_possibilities[len(self.all_possibilities) - 1].append(base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, start, base_domino.second_num)
                        self.all_possibilities.append(self.all_possibilities[len(self.all_possibilities) - 1].copy().pop(len(self.domino_chain) - 1))
                        self.domino_chain.pop(len(self.domino_chain) - 1)
                        self.free_domino_list.insert(0, base_domino.reverse_copy())
                    elif base_domino.connectable_right(start):
                        self.domino_chain.insert(0, base_domino)
                        self.all_possibilities[len(self.all_possibilities) - 1].insert(0, base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, base_domino.first_num, finish)
                        self.all_possibilities.append(self.all_possibilities[len(self.all_possibilities) - 1].copy().pop(0))
                        self.domino_chain.pop(0)
                        self.free_domino_list.insert(0, base_domino)
                    else:
                        base_domino.reverse()
                        self.domino_chain.insert(0, base_domino)
                        self.all_possibilities[len(self.all_possibilities) - 1].insert(0, base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, base_domino.first_num, finish, )
                        self.all_possibilities.append(
                        self.all_possibilities[len(self.all_possibilities) - 1].copy().pop(self.domino_chain[0]))
                        self.domino_chain.pop(0)
                        self.free_domino_list.insert(0, base_domino.reverse_copy())
                    self.current_len += 1


def main():
    domino_num = int(input())
    domino_chain = DominoChain(domino_num)
    domino_chain.create_chain()
    print(domino_chain)
    print(domino_chain.max_len)


main()
