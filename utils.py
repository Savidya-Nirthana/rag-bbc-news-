from typing import Union, List, Dict

def print_object_properties(obj: Union[dict, list]) -> None:
    t = ''
    if isinstance(obj, dict):
        keys = list(obj.keys())
        keys.sort()
        for x in keys:
            y = obj[x]
            if x == 'article_content':
                t += f'{x}: {y[:100]}...(truncated)\n'
            elif x == 'main_vector':
                t+= f'{x}: {y[:30]}...(truncated)\n'
            elif x == 'chunk':
                t+= f'{x}: {y[:100]}...(truncated)\n'

            else:
                t+= f'{x}: {y}\n'
    else:
        for l in obj:
            print_object_properties(l)
        
    print(t)