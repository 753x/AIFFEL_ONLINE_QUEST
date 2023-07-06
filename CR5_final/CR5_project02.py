menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']    # menu 리스트 생성
price = [2000, 3000, 3000, 2500, 2500, 3000]                                      # price 리스트 생성

class Kiosk:
    def __init__(self):
        self.menu = menu
        self.price = price

    # 메뉴 출력 메서드
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i+1, self.menu[i], ':',self.price[i])

    # 주문 메서드
    def menu_select(self):
        self.order_menu = []
        self.order_price = []

        n = 0
        while n < 1 or len(menu) < n:
            n = int(input('음료 번호를 입력하세요: '))

            if 1 <= n <= len(menu):
                self.order_price.append(self.price[n-1])
                self.price_sum = self.price[n-1]
            else:
                print("없는 메뉴입니다. 다시 주문해 주세요.")
    
        t = 0
        while t != 1 and t != 2:
            t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요: "))
            if t == 1:
                self.temp = 'HOT'
            elif t == 2:
                self.temp = 'ICE'
            else:
                print('1과 2 중 하나를 입력하세요')
        self.order_menu.append(self.temp + ' ' + self.menu[n-1])
        print(self.temp, self.menu[n-1], ' : ', self.price_sum, '원')

        while n != 0:
            print()
            n = int(input('추가 주문은 음료 번호를, 지불은 0을 누르세요: '))
            if n > 0 and n < len(self.menu) + 1:
                t = 0
                while t != 1 and t != 2:
                    t = int(input('추가 주문 음료의 온도를 입력하세요 (HOT: 1, ICE: 2): '))
                    if t == 1:
                        temp = 'HOT'
                    elif t == 2:
                        temp = 'ICE'
                    else:
                        print('1과 2 중 하나를 입력하세요.\n')
                self.order_price.append(self.price[n-1])
                self.order_menu.append(temp + ' '+ self.menu[n-1])
                self.price_sum += self.price[n-1]
                print('추가 주문 음료', temp, self.menu[n-1], ' : ', self.price[n-1], '원\n', '합계 : ', self.price_sum, '원')
            
            elif n == 0:
                print('주문이 완료 되었습니다.')
                print(self.order_menu, self.order_price)
            else:
                print('없는 메뉴입니다. 다시 주문해 주세요.')
    
    # 지불
    def pay(self):
        print(f'총 합계 금액은 {self.order_price} 입니다.')
        self.pay_method = 0
        while self.pay_method != 1 and self.pay_method != 2:
            self.pay_method = int(input('1 or 2: '))
            if self.pay_method == 1:
                print('직원에게 문의해 주세요')
            elif self.pay_method == 2:
                print('IC칩 방향에 맞게 카드를 꽂아주세요')
            else:
                print('다시 입력하세요')

    # 주문서 출력 
    def table(self):
        outline1 = '⟝'+'-'*30+'⟞'
        outline2 = '|' + ' ' * 31+ '|'

        print(outline1)
        for i in range(5):
            print(outline2)

        for i in range(len(self.order_menu)):
            print(self.order_menu[i], ' : ', self.order_price[i])

        print('합계 금액 : ', self.price_sum)

        for i in range(5):
            print(outline2)
        print(outline1)

a = Kiosk()  # 객체 생성 
a.menu_print()  # 메뉴 출력
a.menu_select()  # 주문
a.pay()  # 지불
a.table()  # 주문표 출력1
