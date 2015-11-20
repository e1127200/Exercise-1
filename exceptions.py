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
Module for testing exception handling
'''

######################
# Raising Exceptions #
######################

# Use the function search_n from the functions module inside a new function
# also named search_n. The function should do the same as functions.search_n
# but if the variable is not found in the list then raise a ValueError.
def search_n(things, item):
    """
    proofes, if a variable can be found within a given list of numbers and strings
    - if not it raises a ValueError
    - else it returns the tuple of the index where the variable was found  and
    the variable itself
    Parameters
    ----------
    things: list
        list to search in
    item: integer, float_number or string
    Returns
    ----------
    found: a_tuple
        (index, variable)
    """
    i = 0
    while i < len(things):
        if item == things[i]:
            found = (i, item)
            return found
            break
        else:
            i += 1
    else:
        raise ValueError
            
########################
# Excepting Exceptions #
########################

# Define a function called safe_divide which takes two arguments and divides
# the first by the second. This function should handle exceptions that might
# occur print out what went wrong and return None if no results could be
# computed.
def safe_divide(first, second):
    """
    divides the first argument by the second if possible - else it prints out
    what went wrong and returns None
    Parameters
    ----------
    first: integer, float_number
        dividend
    second: integer, float_number
        divisor
    Returns
    ----------
    quotient: integer, float_number
        result
    """
    try:
        quotient = first / second
    except ZeroDivisionError:
        print ("You can not devide by zero.")
        return None
    except TypeError:
        print ("You can not calculate with Strings. Use numbers.")
        return None
    else:
        return quotient