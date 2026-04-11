#!/usr/bin/python3
"""
Bu modul list sinfindən miras alan MyList sinfini təyin edir.
"""


class MyList(list):
    """
    Standart list sinfindən törəmiş xüsusi sinif.
    """

    def print_sorted(self):
        """
        Siyahının elementlərini artan sıra ilə çeşidlənmiş formada çap edir.
        """
        print(sorted(self))
