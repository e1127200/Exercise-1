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
Exercises for using the datetime and the calendar module
'''

# Define a function named last_of_month that takes an argument dt of type date
# and returns a date object representing the last day of the month dt was in.
from datetime import date
def last_of_month(dt):
    """
    takes an argument dt of type date and returns a date object representing
    the last day of the month dt was in (takes into consideration leap years)
    Parameters
    ----------
    dt: date
        determines month
    Returns
    -------
    lday: date
        last day of this month
    """
    short = [4, 6, 9, 11]
    if dt.month in short:
        day = 30
    elif dt.month == 2:
        if dt.year % 400 == 0 or dt.year % 4 == 0 and dt.year % 100 != 0:
            day = 29
        else:
            day = 28
    else:
        day = 31
    lday = date(dt.year, dt.month, day)
    return lday
   
# Define a function named feed_the_gremlin which takes a time object as an
# argument. It should return False between midnight and 6:30AM and True
# otherwise.
def feed_the_gremlin(tm):
    """
    takes a time object as an argument and returns False between midnight and 
    6:30AM and True otherwise
    Parameters
    ----------
    tm: time
        time to check
    Returns
    -------
    yn: boolean
        true/false answer
    """
    sec = tm.hour * 3600 + tm.minute * 60 + tm.second  
    if sec < 23400 and sec > 0:
        return False
    else:
        return True

# Define a function named how_long that takes two datetime objects dt and ref
# where ref is the reference datetime, calculates the difference between them and
# returns the difference as a string formatted like:
# "01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
# If ref is before dt then use 'since' instead of 'until'
def how_long(dt, ref):
    """
    takes two datetime objects dt and ref where ref is the reference datetime,
    calculates the difference between them and returns the difference as a string
    formatted like:"01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
    Parameters
    ----------
    dt: datetime
        new datetime
    ref: datetime
        refernce datetime
    Returns
    -------
    diff: string
        formated time difference
    """  
    if dt > ref:
        diff = dt - ref
        diffd = str(diff.days).zfill(2)
        diffm = str(diff.seconds // 60).zfill(2)
        diffs = str(diff.seconds % 60).zfill(2)
        reff = ref.strftime("%Y-%m-%d %H:%M:%S")
        return "{} days, {} minutes, {} seconds since {}".format(diffd, diffm, diffs, reff)
    elif dt < ref:
        diff = ref - dt
        diffd = str(diff.days).zfill(2)
        diffm = str(diff.seconds // 60).zfill(2)
        diffs = str(diff.seconds % 60).zfill(2)
        reff = ref.strftime("%Y-%m-%d %H:%M:%S")
        return "{} days, {} minutes, {} seconds until {}".format(diffd, diffm, diffs, reff)
    else:
        return "There is no time differnce!"