import re
from utils import Parser

class DumpParser(Parser):
    regex_lut_begin = re.compile(r'^LUT\:\s*([\w\s\-\_]+)\s+Table\:\s*([\w\-]+)\s+Size\s*\=\s*(\d+)\s+Precision\s+(\d+)')

    def __init__(self):
        self.init = self.f_search

    def f_search(self, state):
        """Search for next LUT"""
        result = self.regex_lut_begin.match(state.line)
        if result:
            name = result.group(1).strip()
            table = result.group(2)
            size = result.group(3)
            precision = result.group(4)
            state.create(' '.join((name, table)))
            state.lut.size = size
            state.lut.precision = precision
            self.mode = self.f_skip

    def f_skip(self, state):
        """Skip line"""
        self.mode = self.f_read

    def f_read(self, state):
        """Read single value"""
        if state.line.startswith("Element"):
            value = int(state.line.split()[2])
            state.append(value)
        else:
            state.push()
            self.mode = self.f_search

if __name__ == '__main__':
    parser = DumpParser()
    with open("dump_LUTS.log") as f:
        luts = parser.parse(f)

    for lut in luts:
        print(lut.name)
        print(lut.data)
        print(len(lut.data))

