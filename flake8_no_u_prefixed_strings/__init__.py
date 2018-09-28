"""Define a flake8 plugin to check for invalid escape sequences."""

__version__ = '0.1'

from token import STRING


# noinspection PyUnusedLocal
def plugin(tree, file_tokens):
    """Walk the tree and detect u-prefixed strings."""
    for token_type, token_string, start, end, line in file_tokens:
        if token_type is not STRING:
            continue
        # token[1] == token.string # python 3
        prefix = token_string[:token_string.find(token_string[-1])].lower()
        # print(prefix)
        if 'u' in prefix:
            yield (
                start[0],  # line_number
                start[1],  # offset
                'U001: u-prefixed string ' + repr(token_string)[1:-1],  # text
                None  # check # unused
            )


plugin.name = 'flake8-no-u-prefixed-strings'
plugin.version = __version__
