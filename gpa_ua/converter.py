def ua_to_us(mark):
    """
    Converting Ukrainian marks to US marks
    :param mark: mark, integer between 0 and 100
    :return: integer between 0 and 4
    """
    if 0 <= mark < 50:       # F
        return 0
    elif 50 <= mark < 70:    # C
        return 2
    elif 70 <= mark < 90:    # B
        return 3
    elif 90 <= mark <= 100:  # A
        return 4
    else:
        raise ValueError('Mark must be between 0 and 100 (both inclusive)')


def _gpa(df, marks, only_exams):
    """
    Computes gpa using only exams or all marks
    :param df: pandas.DataFrame with columns 'credits', 'hours', 'exam'
    :param marks: marks (Ukrainian or US)
    :param only_exams: bool
    :return: prints 4 GPA values (exams/all marks, credits/hours)
    """
    if only_exams:
        print('\tUsing only exams: ', end='')
        mask = df['exam'] == 1
        df = df[mask]
        marks = marks[mask]
    else:
        print('\tUsing all marks: ', end='')
    print('{:.2f}'.format((df['hours'] * marks).sum() / df['hours'].sum()))


def gpa(df, use_us):
    """
    Computes gpa for given data.
    :param df: pandas.DataFrame having columns 'credits', 'hours', 'exam', 'marks'
    :param use_us: bool (whether to convert Ukrainian marks to US marks)
    :return: calls _gpa and prints GPA values
    """
    if use_us:
        print('Converting to US marks:')
        marks = df['marks'].map(ua_to_us)
        _gpa(df, marks, only_exams=True)
        _gpa(df, marks, only_exams=False)
    else:
        print('Using Ukrainian marks:')
        marks = df['marks']
        _gpa(df, marks, only_exams=True)
        _gpa(df, marks, only_exams=False)


if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('data.csv')
    for col in ['hours', 'marks', 'exam']:
        if col not in df.columns:
            raise RuntimeError('File must contain `{}` column'.format(col))
    gpa(df, use_us=False)
    gpa(df, use_us=True)
