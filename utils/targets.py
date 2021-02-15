__all__ = ['isExtremelyRisky', 'isAverage', 'isLowEnd', 'isHighEnd']

def isExtremelyRisky(row):
    if (row['BMI_Wt']=='overweight') or (row['Old_Young']=='old')  or (row['Thin_Fat']=='fat'):
        val='extremely_risky'
    else:
        val='not_extremely_risky'
    return val

def isAverage(row):
    if (row['BMI_Wt']=='average') or (row['Old_Young']=='average')  or (row['Thin_Fat']=='average') or (row['Short_Tall']=='average'):
        val='average'
    else:
        val='non_average'
    return val

def isLowEnd(row):
    if (row['BMI_Wt']=='under_weight') or (row['Old_Young']=='young')  or (row['Thin_Fat']=='thin') or (row['Short_Tall']=='short'):
        val='low_end'
    else:
        val='non_low_end'
    return val

def isHighEnd(row):
    if (row['BMI_Wt']=='overweight') or (row['Old_Young']=='old')  or (row['Thin_Fat']=='fat') or (row['Short_Tall']=='tall'):
        val='high_end'
    else:
        val='non_high_end'
    return val