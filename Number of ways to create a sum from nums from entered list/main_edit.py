from visualiser.visualiser import Visualiser as vs


def program(required_sum):
    num_list = list(range(1, required_sum))

    def find(N, M):
        if N == -1 and M == 0: return 1
        if N == -1 and M != 0: return 0
        if M == num_list[N]:
            if N >= 1:
                return 1 + find(N-1, M)
            else:
                return 1
        if M - num_list[N] > 0:
            return find(N - 1, M) + find(N - 1, M - num_list[N])
        else:
            return find(N - 1, M)

    return find(len(num_list) - 1, required_sum)


input_sum = int(input())
print(program(input_sum))
