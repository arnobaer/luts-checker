import sys

def log(*args, **kwargs):
    color = "\033[0m"
    if 'color' in kwargs:
        if kwargs['color'] == 'red':
            color = "\033[31m"
        if kwargs['color'] == 'green':
            color = "\033[32m"
    if sys.stdout.isatty():
        sys.stdout.write(color)
    sys.stdout.write(" ".join([format(arg) for arg in args]))
    if sys.stdout.isatty():
        sys.stdout.write("\033[0m")
    sys.stdout.write("\n")

class Lut:

    def __init__(self, name):
        self.name = name
        self.data = []

class Parser:

    init = None

    class State:
        def __init__(self):
            self.luts = []
            self.lut = None
            self.line = None
        def load(self, line):
            """Load next line to parse."""
            self.line = line.strip() # sanitize
        def create(self, name):
            """Create new LUT buffer."""
            self.lut = Lut(name)
        def push(self):
            """Push current LUT to stack and reset current LUT."""
            self.luts.append(self.lut)
            self.lut = None
        def append(self, *values):
            """Append one or more values to current LUT."""
            self.lut.data.extend(values)

    def parse(self, f):
        """Parse file stream, returns list of parsed LUTs."""
        state = self.State()
        self.mode = self.init
        for line in f:
            state.load(line)
            self.mode(state)
        return state.luts
