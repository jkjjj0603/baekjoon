import sys

def solve():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []

    for _ in range(t):
        n = int(input().strip())          # ✅ 8896은 n만 입력
        robots = [input().strip() for _ in range(n)]
        k = len(robots[0])                # ✅ k는 문자열 길이

        alive = set(range(n))             # 살아있는 로봇 인덱스(0~n-1)

        for r in range(k):                # r번째 라운드
            if len(alive) <= 1:
                break

            choices = {robots[i][r] for i in alive}  # 이번 라운드에 나온 손 종류

            # 무효 라운드: 한 종류만 나오거나, 세 종류 다 나오면 아무도 탈락 X
            if len(choices) == 1 or len(choices) == 3:
                continue

            # 두 종류만 나온 경우: 승자/패자 결정
            if choices == {'R', 'S'}:
                loser = 'S'
            elif choices == {'S', 'P'}:
                loser = 'P'
            else:  # {'P', 'R'}
                loser = 'R'

            # 패자 낸 로봇 제거 (set 순회 중 삭제하면 위험하니 리스트로 따로 뽑음)
            to_remove = [i for i in alive if robots[i][r] == loser]
            for i in to_remove:
                alive.remove(i)

        if len(alive) == 1:
            out.append(str(next(iter(alive)) + 1))   # 1-index로 출력
        else:
            out.append("0")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()