menu = ['', 'Single Regular', 'Single King', 'Double Junior', 'Double Regular', 'Pint', 'Quarter', 'Family', 'Half Gallon']
price = [0, 3200, 4000, 4300, 4300, 6200, 8200, 15500, 22000, 26500]
corn = ['', 'cup', 'corn']
flavor = ['', '치즈나무숲', '치즈고구마구마', '찰떡콩떡', '체다치즈앤포테이토', '오레오쿠키앤크림', '월넛', '오레오쿠키앤밀크',
          '파핑파핑바나나', '에스프레소앤크림','엄마는외계인', '쫀떡궁합', '너는참달고나', '허니치즈트랩', '아몬드봉봉', '마법사의할로윈',
          '민트초콜릿칩', '슈팅스타', '사랑에빠진딸기', '뉴욕치즈케이크', '피스타치오아몬드', '베리베리스트로베리', '바람과함께사라지다',
          '레인보우샤베트', '자모카아몬드훠지', '이상한나라의솜사탕', '초콜릿', '31요거트', '그린티', '체리쥬빌레', '바닐라', '초콜릿무스']
bill = [0, 10000, 5000, 1000]
print("어서오세요. 베스킨라빈스입니다.")

def menu_print():
    i = 1
    while i < len(menu):
        print("%d. %-20s %5d"% (i, menu[i], price[i]))
        i = i+1
    print()
        
def menu_select():
    n = int(input("아이스크림 종류를 선택하세요 : "))
    price_sum = price[n]
    print(menu[n], price[n], '원 ', '합계 ', price_sum, '원')
    print()
    def flavor_print(): 
            i = 1
            while i < len(flavor):
                print("%d.%s"% (i, flavor[i]), end = '   ')
                i = i+1
    flavor_print()
    print()
    def flavor_select():
        n = int(input("맛을 선택하세요 : "))
        print(flavor[n])
    print()
    flavor_select()             
            
    if n >= 3 and n <= 4:
        flavor_select()
    if n == 5:
        flavor_select()
        flavor_select()
    if n == 6:
        flavor_select()
        flavor_select()
        flavor_select()
    if n == 7:
        flavor_select()
        flavor_select()
        flavor_select()
        flavor_select()
    if n == 8:
        flavor_select()
        flavor_select()
        flavor_select()
        flavor_select()
        flavor_select()        
    print()
    if n > 0 and n <= 4:
        n = int(input("컵은 1, 콘은 2를 누르세요 : "))
        print(corn[n])

    while n != 0:        
        n = int(input("계속 주문은 아이스크림 종류 번호를, 지불은 0을 누르세요 : "))
        if n > 0 and n < len(menu):
            price_sum = price_sum + price[n]
            print(menu[n], price[n], '원', '합계', price_sum, '원')
            flavor_select()
            if n >= 3 and n <= 4:
                flavor_select()
            if n == 5:
                flavor_select()
                flavor_select()
            if n == 6:
                flavor_select()
                flavor_select()
                flavor_select()
            if n == 7:
                flavor_select()
                flavor_select()
                flavor_select()
                flavor_select()
            if n == 8:
                flavor_select()
                flavor_select()
                flavor_select()
                flavor_select()
                flavor_select()
            print()   
            if n > 0 and n<=4:
                n = int(input("컵은 1, 콘은 2를 누르세요 : "))
                print(corn[n])
                print()        
        else:
            if n == 0 :
                print("주문이 완료되었습니다.")
            else:
                print("없는 메뉴입니다.")
    return price_sum
def menu_pay(total_price):
    for i in range (1, len(bill)):
        print(i, '.', bill[i], '원', end='    ')
    print()
    pay = 0
    while pay < total_price:
        n = int(input("지불 금액을 입력하세요 : "))
        if n>0 and n<len(bill):
            pay = pay + bill[n]
            print('총 지불액 :', pay, '원')
        else :
            print('다시 선택하세요.')
    print('거스름 ', pay-total_price, '원')
print()
menu_print()
total_price = menu_select()
menu_pay(total_price)
print("감사합니다. ")
