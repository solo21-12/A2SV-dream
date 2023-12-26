def team_olympiad(nums):
    programming, maths, pe = [], [], []

    # Separate students based on their skills
    for i, num in enumerate(nums):
        if num == 1:
            programming.append(i + 1)
        elif num == 2:
            maths.append(i + 1)
        else:
            pe.append(i + 1)

    # Calculate the maximum number of teams possible
    max_teams = min(len(programming), len(maths), len(pe))

    print(max_teams)

    # Form teams
    for i in range(max_teams):
        print(programming[i], maths[i], pe[i])

n = int(input())
nums = list(map(int, input().split()))

team_olympiad(nums)
