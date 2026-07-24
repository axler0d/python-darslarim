talaba = {
"Ali":[5,4,3],
"Vali":[4,5,5],
"Hasan":[3,2,4]
}
for ism, baholar in talaba.items():
    print(f"{ism}ning o'rtacha bahosi: {sum(baholar)/len(baholar)}")
    