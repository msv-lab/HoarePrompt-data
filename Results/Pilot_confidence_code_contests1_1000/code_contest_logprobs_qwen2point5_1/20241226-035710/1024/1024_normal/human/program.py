from operator import itemgetter

N_shop, M_required_drink  = map(int, raw_input().split())

shop_list = []
for tmp_shop in range(N_shop):
  shop_list.append(map(int, raw_input().split()))

total_money = 0
got_drink = 0
for i in sorted(shop_list, key=itemgetter(0)):
  limit_at_shop = i[1]
#  print(i)

  while got_drink < M_required_drink and limit_at_shop > 0:
    total_money = total_money + i[0]
    got_drink   = got_drink + 1
    limit_at_shop = limit_at_shop - 1
#    print("  %s %s %s" % (total_money, got_drink, limit_at_shop))

print(total_money)
