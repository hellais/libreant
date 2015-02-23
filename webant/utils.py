import re
import functools


def memoize(obj):
    '''decorator to memoize things'''
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


def requestedFormat(request, acceptedFormat):
        """Return the response format requested by client

        Client could specify requested format using:
        (options are processed in this order)
            - `format` field in http request
            - `Accept` header in http request
        Example:
            chooseFormat(request, ['text/html','application/json'])
        Args:
            acceptedFormat: list containing all the accepted format
        Returns:
            string: the user requested mime-type (if supported)
        Raises:
            ValueError: if user request a mime-type not supported
        """
        if 'format' in request.args:
            fieldFormat = request.args.get('format')
            if fieldFormat not in acceptedFormat:
                raise ValueError("requested format not supported: %s" %
                                 fieldFormat)
            return fieldFormat
        else:
            return request.accept_mimetypes.best_match(acceptedFormat)


_snake_case_re_one = re.compile('(.)([A-Z][a-z]+)')
_snake_case_re_two = re.compile('([a-z0-9])([A-Z])')


def snake_case(camel_str):
    """
    Returns a snake case string based on a camel case input.

    Example: CamelCaseString -> camel_case_string
    """
    s = _snake_case_re_one.sub(r'\1_\2', camel_str)
    return _snake_case_re_two.sub(r'\1_\2', s).lower()


def camel_case(snake_str):
    """
    Returns a string in camel case based on a snake case string.

    Example: snake_case_string -> SnakeCaseString
    """
    components = snake_str.split('_')
    return "".join(x.title() for x in components)
