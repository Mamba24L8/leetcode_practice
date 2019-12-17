# -*- coding: utf-8 -*-
"""
Created on 12/17/19 6:10 PM

@author: mamba

@purpose：
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """两数之和

    Parameters
    ----------
    nums : List[int]
    target : int

    Examples
    --------
    >>> nums = [3, 4, 5, 7, 10]
    >>> target = 11
    >>> two_sum(nums, target)
    [1, 3]
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    """
    hash_map = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hash_map:
            return [hash_map[another_num], index]
        hash_map[num] = index


def word_pattern(words: List[str], nums: List[int]) -> bool:
    """单词匹配

    Parameters
    ----------
    words
    nums

    Examples
    --------
    >>> word_pattern(["苹果", "香蕉", "香蕉", "苹果"], [1, 2, 2, 1])
    True
    >>> word_pattern(["香蕉", "苹果", "香蕉", "苹果"], [1, 2, 2, 1])
    False
    """
    hash_map = {}
    for word, num in zip(words, nums):
        if word in hash_map:
            if hash_map[word] != num:
                return False
        hash_map[word] = num
    if len(hash_map) == len(set(nums)):
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
