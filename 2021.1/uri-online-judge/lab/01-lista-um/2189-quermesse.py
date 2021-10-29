results = []
cases = 0


def newCase(cases):
    cases += 1
    guestsNumber = int(input())
    if guestsNumber != 0:
        guests = list(map(int, input().split()))
        for index, guest in enumerate(guests):
            if (index + 1) == guest:
                results.append(f"Teste {cases}")
                results.append(guest)
                results.append("")
        newCase(cases)
    else:
        for result in results:
            print(result)


newCase(cases)
