

"""pass"""

import crawl
OBJS = [
    crawl.MeiZiTu
    ]

def start_function(class_obj):
    """pass"""
    return class_obj().main()

if __name__ =='__main__':
    for obj in OBJS:
        start_function(obj)