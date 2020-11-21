

products = [{"name":"Samsung s6", "price":"3000"},
            {"name":"Samsung s7", "price":"4000"},
            {"name":"Samsung s8", "price":"5000"},
            {"name":"Samsung s9", "price":"6000"},
            {"name":"Samsung 10", "price":"7000"}
              ]
total = 0
for i in products:
  total = total + int(i["price"])
print(total)