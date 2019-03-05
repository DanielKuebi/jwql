"""This module holds functions for miri data trending

All functions in this module are tailored for the miri datatrending application.
Detailed descriptions are given for every function individually.

-------
    - Daniel Kühbacher

Use
---

Dependencies
------------
MIRI_trend_requestsDRAFT1900201.docx

References
----------

Notes
-----

"""

import jwql.instrument_monitors.nirspec_monitors.data_trending.utils.mnemonics as mn
import jwql.instrument_monitors.nirspec_monitors.data_trending.utils.condition as cond
import statistics
import sqlite3
import warnings
from collections import defaultdict



def extract_data(condition, mnemonic):
    '''Function extracts data from given mnemmonic at a given condition
    Parameters
    ----------
    condition : object
        conditon object that holds one or more subconditions
    mnemonic : AstropyTable
        holds single table with mnemonic data
    Return
    ------
    temp : list  or None
        holds data that applies to given condition
    '''
    temp = []

    #look for all values that fit to the given conditions
    for element in mnemonic:
        if condition.state(float(element['time'])):
            temp.append(float(element['value']))

    #return temp is one ore more values fit to the condition
    #return None if no applicable data was found
    if len(temp) > 0:
        return temp
    else:
        return None

def whole_day_routine(mnemonic_data):
    '''Proposed routine for processing a 15min data file once a day
    Parameters
    ----------
    mnemonic_data : dict
        dict holds time and value in a astropy table with correspining identifier as key
    Return
    ------
    data_cond_1 : dict
        holds extracted data with condition 1 applied
    data_cond_1 : dict
        holds extracted data with condition 2 applied
    '''

    #abbreviate attribute
    m = mnemonic_data

    #########################################################################
    con_set_1 = [                                               \
    cond.unequal(m.mnemonic('INRSD_EXP_STAT'),'STARTED')]

    #setup condition
    condition_1 = cond.condition(con_set_1)

    data_cond_1 = dict()

    #add filtered engineering values of mnemonics given in list mnemonic_cond_1
    #to dictitonary
    for identifier in mn.mnemonic_cond_1:
        data = extract_data(condition_1, m.mnemonic(identifier))

        if data != None:
            data_cond_1.update( {identifier:data} )
        else:
            print("no data for {}".format(identifier))

    del condition_1

    ##########################################################################
    con_set_2 = [                                                           \
    cond.equal(m.mnemonic('INRSH_LAMP_SEL'), 'NO_LAMP')]
    #setup condition
    condition_2 = cond.condition(con_set_2)

    data_cond_2 = dict()

    #add filtered engineering values of mnemonics given in list mnemonic_cond_2
    #to dictitonary
    for identifier in mn.mnemonic_cond_2:
        data = extract_data(condition_2, m.mnemonic(identifier))

        if data != None:
            data_cond_2.update( {identifier:data} )
        else:
            print("no data for {}".format(identifier))

    del condition_2

    ##########################################################################
    con_set_3 = [                                                           \
    cond.equal(m.mnemonic('INRSI_CAA_ON_FLAG'), 'ON'),                      \
    cond.unequal(m.mnemonic('INRSH_LAMP_SEL'), 'NO_LAMP')]
    #setup condition
    condition_3 = cond.condition(con_set_3)

    data_cond_3 = dict()

    #add filtered engineering values of mnemonics given in list mnemonic_cond_2
    #to dictitonary
    for identifier in mn.mnemonic_cond_3:
        data = extract_data(condition_3, m.mnemonic(identifier))

        if data != None:
            data_cond_3.update( {identifier:data} )
        else:
            print("no data for {}".format(identifier))

    del condition_3

    ##########################################################################
    con_set_4 = [                                                           \
    cond.equal(m.mnemonic('INRSH_WHEEL_MOT_SVREF'), 'REF_ON')]
    #setup condition
    condition_4 = cond.condition(con_set_4)

    data_cond_4 = dict()

    #add filtered engineering values of mnemonics given in list mnemonic_cond_2
    #to dictitonary
    for identifier in mn.mnemonic_cond_4:
        data = extract_data(condition_4, m.mnemonic(identifier))

        if data != None:
            data_cond_4.update( {identifier:data} )
        else:
            print("no data for {}".format(identifier))

    del condition_3

    ##########################################################################
    con_set_4 = [                                                           \
    cond.equal(m.mnemonic('INRSH_WHEEL_MOT_SVREF'), 'REF_ON')]
    #setup condition
    condition_4 = cond.condition(con_set_4)

    data_cond_4 = dict()

    #add filtered engineering values of mnemonics given in list mnemonic_cond_2
    #to dictitonary
    for identifier in mn.mnemonic_cond_4:
        data = extract_data(condition_4, m.mnemonic(identifier))

        if data != None:
            data_cond_4.update( {identifier:data} )
        else:
            print("no data for {}".format(identifier))

    del condition_4

    ##########################################################################
    con_set_5 = [                                                           \
    cond.unequal(m.mnemonic('INRSM_MOVE_STAT'), 'STARTED')]
    #setup condition
    condition_5 = cond.condition(con_set_5)

    data_cond_5 = dict()

    #add filtered engineering values of mnemonics given in list mnemonic_cond_2
    #to dictitonary
    for identifier in mn.mnemonic_cond_5:
        data = extract_data(condition_5, m.mnemonic(identifier))

        if data != None:
            data_cond_5.update( {identifier:data} )
        else:
            print("no data for {}".format(identifier))

    del condition_5

    return data_cond_1, data_cond_2, data_cond_3, data_cond_4, data_cond_5


def whole_day_routine(mnemonic_data):
    '''Proposed routine for processing data representing a whole day
    Parameters
    ----------
    mnemonic_data : dict
        dict holds time and value in a astropy table with correspining identifier as key
    Return
    ------
    data_cond_3 : dict
        holds extracted data with condition 3 applied
    FW_volt : list
        extracted data for IMIR_HK_FW_POS_VOLT
    GW14_volt : list
        extracted data for IMIR_HK_GW14_POS_VOLT
    GW23_volt : list
        extracted data for IMIR_HK_GW23_POS_VOLT
    CCC_volt : list
        extracted data for IMIR_HK_CCC_POS_VOLT
    '''

    #abbreviate attribute
    m = mnemonic_data

    #########################################################################
    con_set_3 = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_ICE_SEC_VOLT1'), 25.0)]
    #setup condition
    condition_3 = cond.condition(con_set_3)

    data_cond_3 = dict()

    #add filtered engineering values of mnemonics given in list mnemonic_cond_3
    #to dictitonary
    for identifier in mn.mnemonic_cond_3:
        data = extract_data(condition_3, m.mnemonic(identifier))

        if data != None:
            data_cond_3.update({identifier:data})
        else:
            print("no data for {}".format(identifier))

    del condition_3

    #########################################################################
    #extract data for IMIR_HK_FW_POS_VOLT under given condition
    con_set_FW = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_FW_POS_VOLT'),250.0)]
    #setup condition
    condition_FW = cond.condition(con_set_FW)
    FW_volt = extract_data(condition_FW, m.mnemonic('IMIR_HK_FW_POS_VOLT'))

    del condition_FW

    #extract data for IMIR_HK_GW14_POS_VOLT under given condition
    con_set_GW14 = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_GW14_POS_VOLT'),250.0)]
    #setup condition
    condition_GW14 = cond.condition(con_set_GW14)
    GW14_volt = extract_data(condition_GW14, m.mnemonic('IMIR_HK_GW14_POS_VOLT'))

    del condition_GW14

    #extract data for IMIR_HK_GW23_POS_VOLT under given condition
    con_set_GW23 = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_GW23_POS_VOLT'),250.0)]
    #setup condition
    condition_GW23 = cond.condition(con_set_GW23)
    GW23_volt = extract_data(condition_GW23, m.mnemonic('IMIR_HK_GW23_POS_VOLT'))

    del condition_GW23

    #extract data for IMIR_HK_CCC_POS_VOLT under given condition
    con_set_CCC = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_CCC_POS_VOLT'),250.0)]
    #setup condition
    condition_CCC = cond.condition(con_set_CCC)
    CCC_volt = extract_data(condition_CCC, m.mnemonic('IMIR_HK_CCC_POS_VOLT'))

    del condition_CCC

    return data_cond_3, FW_volt , GW14_volt, GW23_volt, CCC_volt


def wheelpos_routine(mnemonic_data):
    '''Proposed routine for positionsensors each day
    Parameters
    ----------
    mnemonic_data : dict
        dict holds time and value in a astropy table with correspining identifier as key
    Return
    ------
    FW : dict
        holds FW ratio values and times with corresponding positionlabel as key
    GW14 : dict
        holds GW14 ratio values and times with corresponding positionlabel as key
    GW23 : dict
        holds GW23 ratio values and times with corresponding positionlabel as key
    CCC : dict
        holds CCC ratio values and times with corresponding positionlabel as key
    '''

    #abbreviate attribute
    m = mnemonic_data

    con_set_FW = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_FW_POS_VOLT'),250.0)]
    #setup condition
    condition_FW = cond.condition(con_set_FW)
    FW = extract_filterpos(condition_FW, mn.fw_nominals, \
        m.mnemonic('IMIR_HK_FW_POS_RATIO'), m.mnemonic('IMIR_HK_FW_CUR_POS'))

    del condition_FW

    con_set_GW14 = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_GW14_POS_VOLT'),250.0)]
    #setup condition
    condition_GW14 = cond.condition(con_set_GW14)
    GW14 = extract_filterpos(condition_GW14, mn.gw14_nominals, \
        m.mnemonic('IMIR_HK_GW14_POS_RATIO'), m.mnemonic('IMIR_HK_GW14_CUR_POS'))

    del condition_GW14

    con_set_GW23 = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_GW23_POS_VOLT'),250.0)]
    #setup condition
    condition_GW23 = cond.condition(con_set_GW23)
    GW23 = extract_filterpos(condition_GW23, mn.gw23_nominals, \
        m.mnemonic('IMIR_HK_GW23_POS_RATIO'), m.mnemonic('IMIR_HK_GW23_CUR_POS'))

    del condition_GW23

    con_set_CCC = [                                               \
    cond.greater(m.mnemonic('IMIR_HK_CCC_POS_VOLT'),250.0)]
    #setup condition
    condition_CCC = cond.condition(con_set_CCC)
    CCC = extract_filterpos(condition_CCC, mn.ccc_nominals, \
        m.mnemonic('IMIR_HK_CCC_POS_RATIO'), m.mnemonic('IMIR_HK_CCC_CUR_POS'))

    del condition_CCC

    return FW, GW14, GW23, CCC


if __name__ =='__main__':
    pass
