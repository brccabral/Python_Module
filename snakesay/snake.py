SNAKE = r"""  \
   \    __
    \  {oo}
       (__)\ 
         λ \\ 
           _\\__
          (_____)_
         (________)Oo॰
"""


def bubble(message):
    buuble_length = len(message) + 2
    return f"""
 {"_" * buuble_length}
( {message} )
 {"‾" * buuble_length}"""


def say(message):
    print(bubble(message))
    print(SNAKE)