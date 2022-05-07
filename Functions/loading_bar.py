def loading_bar(number):
    percent_signs = number // 10
    if number < 100:
        return f"{number}% [{percent_signs * '%'}{'.' * (10 - percent_signs)}]\nStill loading..."
    else:
        return f'100% Complete!\n[{"%" * 10}]'


number = int(input())
print(loading_bar(number))
