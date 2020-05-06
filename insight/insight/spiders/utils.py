def replace_symbols(text: str = ''):
    """
    Replace Unicode symbols with their ASCII equivalent

    :param text: Initial string
    :return: Result string
    """
    return text.strip().replace('\u2019', "'").replace('\u2014', '-'). \
        replace('\u201c', "'").replace('\u201d', "'").replace('\u00a0', ''). \
        replace('\n', '').replace('\u00ae', 'e®')
