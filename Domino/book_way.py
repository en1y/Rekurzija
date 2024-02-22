class Dominoes:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __repr__(self):
        return f"({self.first_num}, {self.second_num})"

    def __copy__(self):
        return Dominoes(self.first_num, self.second_num)

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
        domino_list = []
        for i in range(domino_num):
            inp = [int(j) for j in input().split()]
            if len(inp) == 2 and 0 < inp[0] <= 6 and 0 < inp[1] <= 6:
                domino_list.append(Dominoes(inp[0], inp[1]))
            else:
                raise TypeError("You have to input 2 elements both of which are in between 1 and 6")
        self.free_domino_list = domino_list.copy()
        self.domino_chain = []

    def create_chain(self, free_dominoes_num, start=0, finish=0, possibility_num = 0):
        for i in range(free_dominoes_num):
            base_domino = self.free_domino_list[i]
            if finish == 0:
                self.domino_chain.append(base_domino)
                self.free_domino_list.pop(i)
                self.create_chain(free_dominoes_num-1, base_domino.first_num, base_domino.second_num)
                self.free_domino_list.insert(0, base_domino)
            else:
                start_finish_domino = Dominoes(start, finish)
                if base_domino.connectable(start_finish_domino):
                    if base_domino.connectable_left(finish):
                        self.domino_chain.append(base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, start, base_domino.second_num)
                        self.free_domino_list.append(base_domino)  # ?????
                    elif base_domino.connectable_right(finish):
                        base_domino = base_domino.reverse()
                        self.domino_chain.append(base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, start, base_domino.second_num)
                        self.free_domino_list.append(base_domino.reverse())
                    elif base_domino.connectable_right(start):
                        self.domino_chain.insert(0, base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, base_domino.first_num, finish)
                        self.free_domino_list.append(base_domino)
                    else:
                        base_domino = base_domino.reverse()
                        self.domino_chain.insert(0, base_domino)
                        self.free_domino_list.pop(i)
                        self.create_chain(free_dominoes_num - 1, base_domino.first_num, finish)
                        self.free_domino_list.append(base_domino.reverse())



def main():
    domino_num = int(input())
    domino_chain = DominoChain(domino_num)
    domino_chain.create_chain(len(domino_chain.free_domino_list))
    print(domino_chain.domino_chain)

main()
