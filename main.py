items = [{

"product_id" : "enchanted_diamond",
"buy_price": 1250,
"sell_price": 1400,
"weekly_volume":500000
},{
    "product_id" : "enchanted_gold",
"buy_price": 800,
"sell_price": 850,
"weekly_volume":200000
}
]



def calculate_spread(items):
    return items["sell_price"] - items["buy_price"]

def profitpot(items):
    calc_spread = calculate_spread(items)
    final = calc_spread * items["weekly_volume"]
    return final

def is_profitable(items):
    return calculate_spread(items) > 100
    



for pickitem in items: 
    full = (pickitem["product_id"], calculate_spread(pickitem), (profitpot(pickitem)))
    if is_profitable(pickitem):
        print (full)
    else: 
        print (is_profitable(pickitem))
        


