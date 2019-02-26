import re
from utils import Parser

class PkgParser(Parser):
    regex_lut_begin = re.compile(r'^\s*constant\s+([\w_]+)\s*\:\s*[\w\_]+\s*\:\=\s*\(')

    def __init__(self):
        self.init = self.f_search

    def f_search(self, state):
        result = self.regex_lut_begin.match(state.line)
        if result:
            name = result.group(1)
            state.create(name)
            self.mode = self.f_read

    def f_read(self, state):
        if state.line.startswith(");"): # end of VHDL array
            state.push()
            self.mode = self.f_search
        else:
            if state.line.startswith("--"):
                return # skip comments
            # Parse line of VHDL array values
            values = [int(value.strip()) for value in state.line.split(",") if value != '']
            state.append(*values)

if __name__ == '__main__':
    parser = PkgParser()
    with open("lut_pkg.vhd") as f:
        luts = parser.parse(f)

    for lut in luts:
        print(lut.name)
        print(lut.data)
        print(len(lut.data))

