# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
In this module you will define several functions.

Please document your functions according to
https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
'''

# Example so that you can see a passing test


def f():
    """Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################

# Define a function named add that takes two numbers and returns the sum.
def add(a, b):
    """
    takes 2 numbers and returns the sum
    """
    return a+b

# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.
def to_tuple(a, b, c):
    """
    takes 3 arguments and returns a tuple of these 3
    """
    return (a, b, c)

# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.
def check5(number):
    """
    checks if the number is greater than 5 (True) or not (False)
    """
    if number > 5:
        return True
    else:
        return False

# Define a function named check_n that check is a number is greater than n. The
# number should be the first argument and n the second
def check_n(number, n):
    """
    checks if the number is greater than n (True) or not (False)
    """
    if number > n:
        return True
    else:
        return False

#########
# LISTS #
#########

# Define a function named check_list that takes two arguments. The first
# argument is a list of numbers and the second argument is the number n to
# compare against. The function should return a list with equal length as the
# input list containing for each number in the original list either True or
# False if the number was greater than or equal to n.
def check_list(numbers, n):
    """
    checks for every number of a list if it is greater than or equal to the
    given number n (True) or not (False)
    Paramters
    ----------
    numbers: list
        numbers to compare
    n: integer, float_number
        number to compare with
    Returns
    ----------
    answer: list
        true/false answers
    """
    i = 0  
    answer = []
    for number in numbers:
        answer.append(number >= n)
    return answer

# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.
def check_list_nth(numbers, n, nth):
    """
    checks for every nth number of a list if it is greater than or equal to the
    given number n (True) or not (False)
    Paramters
    ----------
    numbers: list
        numbers to compare
    n: integer, float_number
        number to compare with
    nth: integer
        number to count through list
    Returns
    ----------
    answer: list
        true/false answers
    """
    i = 0
    numbers = numbers[::nth]
    answer = []
    for number in numbers:
        answer.append(number >= n)
    return answer

# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.
def add_new_list(l, x):
    """
    adds variable x as last element of list l and returns new list nl without
    modifying the original list l
    """
    nl = l + [x]
    return nl

# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.
def remove_nth(l, nth=2):
    """
    removes every nth element (default = 2) of a list
    """
    newl = list(l)    
    del newl[::nth]
    return newl

# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values
def search_n(l, x):
    """
    searches variable x in the list l and returns a tuple of the index and the
    variable itself (if found) or a tuple of two Nones (if not found)
    Parameters
    ----------
    l: list
        where to search in
    x: any type
        what to search for
    Returns
    ----------
    (): a_tuple
        of index and variable
    """
    if x in l:
        return (l.index(x), x) 
    else:
        return(None, None)

################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.
def args_to_dict(a, b, c):
    """
    takes three arguments and returns a dictionary with the position of the
    arguments as the key (starting at 0) and the argument as the value
    """
    return {0:a, 1:b, 2:c}

# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments
def args_to_dict_general(*args):
    """
    takes n arguments and returns a dictionary with the position of the
    arguments as the key (starting at 0) and the argument as the value
    """
    i = 0
    abc = {}
    for arg in args:
        abc[i] = arg
        i += 1
    return abc

# Define a function named lists_to_dict that takes two lists of equal lenght
# named keys and values and builds a dictionary out of them.
def lists_to_dict(list1, list2):
    """
    builds a dictionary of two lists of equal length
    Parameters
    ----------
    list1: list
        first content (keys)
    list2: list
        second content (values)
    Returns
    ----------
    abc: dict
        of the two lists
    """
    i = 0   
    abc = {}
    for vals in list1:
        abc[vals] = list2[i]
        i += 1
    return abc

# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.
def search_list(lista, listb):
    """
    creates a dictionary of elements of listb found in lista with the index where
    found as key (if nothing found the dictionary is empty)
    Parameters
    ----------
    lista: list
        base content
    listb: list
        searched content
    Returns
    ----------
    abc: dict
        of the content found in both lists
    """
    abc = {}    
    for valb in listb:
        if valb in lista:
            abc[lista.index(valb)] = valb
    return abc

# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.
def dict_to_string(dic, sep):
    """
    creates a string of all strings found in the dictionary separated by the given
    string (if nothing found the string is empty)
    Parameters
    ----------
    dic: dict
        base content
    sep: str
        seperator string
    Returns
    ----------
    answer: string
        sum of all strings from the dic, seperated with the sep string
    """
    answer = ""
    for key,value in dic.items():
        if type(value) is str:
            answer = answer + value + sep
    if answer[-1:] == sep:
        answer = answer[:-1]
    return answer

# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'
def classify_by_type(l):
    """
    separetes the content of a list into a dictionary with the lists "int", "str"
    and "others"
    Parameters
    ----------
    l: list
        content to sort
    Returns
    ----------
    answer: dict
        sorted values into the data type groups integer, string, others
    """
    answer = {'int':[], 'str':[], 'others':[]}
    for item in l:
        if type(item) is int:
            answer['int'].append(item)
        elif type(item) is str:
            answer['str'].append(item)
        else:
            answer['others'].append(item)
    return answer