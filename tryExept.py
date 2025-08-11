"""try: 
    divisão = 10 / 0
    print(divisão)
except:
    print('''não foi possivel realizar esa operação''')"""
"""def divide(x,y):
    try:
        result = x/y
    except zeroDivisionError:
        print("por favor, não ultilize zeros!")
    except:
        print("\833[91m algo deu erado...")
    else:
        print(f"seu resultado é: {result}")
    finally:
        print("\833[92m vamos de novo?")
        divide(13,0)"""
import random 
vale = random.randint(0,2)
match vale:
    case 0:
        print("Zero!")
    case 1:
        print("um!")
    case 2:
        print("dois!")
    case _:
        print("excessão")