with open("input2.txt") as f:
    data = [list(map(int, line.strip().split())) for line in f]


def checksafe(report):
    changesign = []

    for i in range(len(report) - 1):
        currentreport = report[i]
        nextreport = report[i + 1]
        if (currentreport - nextreport) > 0:
            changesign.append(-1)
        elif (currentreport - nextreport) < 0:
            changesign.append(1)
        else:
            changesign.append(0)

    if changesign.count(-1) == 0 or changesign.count(1) == 0:
        for i in range(len(report) - 1):
            currentreport = report[i]
            nextreport = report[i + 1]
            if not (
                abs(currentreport - nextreport) >= 1
                and abs(currentreport - nextreport) <= 3
            ):
                return False
        return True
    else:
        return False


def problemdampener(report):
    if checksafe(report):
        return True
    else:
        for i in range(len(report)):
            remove = report.pop(i)
            if checksafe(report):
                return True
            report.insert(i, remove)
    return False


# part 1
safe = 0

for report in data:
    if checksafe(report):
        safe += 1

print(safe)

# part 2
safe = 0

for report in data:
    if problemdampener(report):
        safe += 1

print(safe)
