SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(4000, a_kilobyte_is_1024_bytes=True):
    '''Преобразует размер файла в удобочитаемую для человека форму.

    Ключевые аргументы:
    size -- размер файла в байтах
    a_kilobyte_is_1024_bytes -- если True (по умолчанию), используются степени 1024
                                если False, используются степени 1000

    Возвращает: текстовую строку (string)

    '''
    if size < 0:
        raise ValueError('число должно быть неотрицательным')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('число слишком большое')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
