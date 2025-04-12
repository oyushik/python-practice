money = 10000
people = 3
money_per_person = int(money / people)
change = money % people
print(f"각자 {money_per_person}원을 받고 {change}원이 남습니다.")
