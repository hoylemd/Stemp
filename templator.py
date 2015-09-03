import re


class Stemp(object):
    def __init__(self, values):
        self.values = values
        self.token_re = re.compile('&[(]([^)]+?)[)]')

    def apply(self, lines):
        output_lines = []
        for line in lines:
            output_line = line
            tokens = self.token_re.findall(output_line)
            if tokens:
                for token in tokens:
                    value = self.values[token]
                    token_pattern = '&\(' + token + '\)'
                    edited = re.subn(token_pattern, value, output_line)
                    output_line = edited[0]
            else:
                output_line = line

            output_lines.append(output_line)

        return output_lines
