#!/usr/bin/python3
"""
Bu modul obyektin tam olaraq müəyyən bir sinfə 
aid olub-olmadığını yoxlayan funksiyanı ehtiva edir.
"""


def is_same_class(obj, a_class):
    """
    Obyektin tam olaraq verilmiş sinfin nüsxəsi olub-olmadığını yoxlayır.
    
    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.
        
    Returns:
        Tam uyğundursa True, əks halda False.
    """
    return type(obj) is a_class
