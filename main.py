from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def cafe_program():
  menu = Menu()
  coffee_maker = CoffeeMaker()
  money_machine = MoneyMachine()

  # 주문을 완료했다면 다시 주문을 할 수 있도록 해야 함.
  while True:
    # TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    # 사용자에게 음료 주문 받기

    order = input(f"What would you like? {menu.get_items()}: ")

    # TODO: Turn off the Coffee Machine by entering “off” to the prompt.
    # 주문을 받을 때 사용자가 'off'를 누르면 종료.
    if order == 'off':
      break

    # TODO: Print report
    # 'report'를 입력하면 현재 재고가 얼마나 남아있는지 출력
    if order == 'report':
      coffee_maker.report()
      # 얼마 벌었는지 표시
      money_machine.report()
    else:
      # TODO: Check resources sufficient?
      # 고객이 주문을 완료하면 음료를 만들 재료가 충분한지 확인.
      # 재료가 충분하지 않다면 “Sorry there is not enough water.” 출력
      drink = menu.find_drink(order_name=order)
      if coffee_maker.is_resource_sufficient(drink):

        # 그대신 다른 메류 주문 권유(이건 일단 보류)

        # TODO: Process coins
        # 재료가 충분하다면 코인을 투입하라고 출력
        # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # 코인의 총합을 구한다.

        # TODO: Check transaction successful?
        # 고객이 지불한 금액이 음료를 사기 충분한지 검사
        # 돈이 충분하지 않다면  “Sorry that's not enough money. Money refunded.” 출력
        # 지불한 금액이 충분하다면 이익으로 계산한다.
        # 고객이 주문한 음료의 재료를 차감하고, 이익이 계산됐는지 'report'로 확인할 수 있어야 한다.
        # 돈을 지불하고 남은 잔돈은 거슬러 줘야 한다.
        order_cost = drink.cost
        money_machine.make_payment(order_cost)

        # TODO: Make Coffee.
        # 음료 주문으로 인해 재료 차감.
        # "Here is your latte. Enjoy!" 상품을 제공할 때 출력
        coffee_maker.make_coffee(drink)


cafe_program()
