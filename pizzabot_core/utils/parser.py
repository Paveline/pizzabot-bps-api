import re


class ParseError(Exception):
    pass


class Parser:
    FIELD_SIZE_2D_RE = re.compile(r'(\d+)x(\d+)')
    POINT_2D_RE = re.compile(r'\((\d+),\s?(\d+)\)')

    @classmethod
    def parse_input_data(cls, string: str):
        string_with_delimiters = string.replace(' (', ';(')
        args = string_with_delimiters.split(';')

        field_size_string = args[0]
        if not field_size_string:
            raise ParseError('Field size can\'t be empty!')
        field_size = cls.__convert_string_to_field_size(field_size_string)

        points_as_strings = args[1:]
        if not points_as_strings:
            raise ParseError('You must input at least one delivery point!')
        points = [cls.__convert_string_to_point(point) for point in points_as_strings]

        return field_size, points

    @classmethod
    def __convert_string_to_point(cls, string: str) -> tuple[int, int]:
        match_obj = re.fullmatch(cls.POINT_2D_RE, string)
        if match_obj is not None:
            x, y = int(match_obj.group(1)), int(match_obj.group(2))
            return x, y
        else:
            raise ParseError(f'Invalid point format {string}.')

    @classmethod
    def __convert_string_to_field_size(cls, string: str) -> tuple[int, int]:
        match_obj = re.fullmatch(cls.FIELD_SIZE_2D_RE, string)
        if match_obj is not None:
            size_x, size_y = int(match_obj.group(1)), int(match_obj.group(2))
            return size_x, size_y
        else:
            raise ParseError(f'Invalid field_size format {string}.')
