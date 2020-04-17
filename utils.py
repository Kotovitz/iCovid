# metadata
__title__ = 'PY_UTILS_LIB'
__version__ = '0.1.0[a]'
__release__ = '17 Apr 2020'
__author__ = 'Oleksandr Viytiv'


class colour:
    ''' Colour class '''
    NORMAL = '\033[0m'      # return normal font style
    BOLD = '\033[01m'       # make text bold
    DISABLE = '\033[02m'    # ???
    UNDERLINE = '\033[04m'  # underline text
    REVERSE = '\033[07m'    # ???
    STRIKE = '\033[09m'     # put strikeline over text
    INVISIBLE = '\033[08m'  # ???

    # foreground colours
    class fg:
        black = '\033[30m'
        grey = '\033[90m'
        red = '\033[31m'
        green = '\033[32m'
        blue = '\033[34m'
        cyan = '\033[36m'
        orange = '\033[33m'
        yellow = '\033[93m'
        purple = '\033[35m'
        pink = '\033[95m'
        lightgrey = '\033[37m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        lightblue = '\033[94m'
        lightcyan = '\033[96m'

    # background colours
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        blue = '\033[44m'
        cyan = '\033[46m'
        orange = '\033[43m'
        purple = '\033[45m'
        lightgrey = '\033[47m'


class logLevel:
    ''' Logging level class '''
    CRITICAL = 0  # component, subsystem crash
    ERROR = 1     # unexpected flow behaviour
    WARNING = 2   # suspicious flow behaviour
    SUCCESS = 3   # successful operation
    NORMAL = 4    # usual log message for user
    DEBUG = 5     # message contain development info
    TRACE = 6     # any trash you want

    # string to describe log level
    token = {CRITICAL: 'CRITICAL',
             ERROR: 'ERROR',
             WARNING: 'Warning',
             SUCCESS: 'Success',
             NORMAL: 'normal',
             DEBUG: 'debug',
             TRACE: 'trace'}

    # color for each log level
    colour = {CRITICAL: colour.bg.purple,
              ERROR: colour.fg.red,
              WARNING: colour.fg.orange,
              SUCCESS: colour.fg.green,
              NORMAL: colour.fg.yellow,
              DEBUG: colour.fg.blue,
              TRACE: colour.fg.lightcyan}


class logger:
    ''' Logger object provide logging subsystem '''
    def __init__(self, gllvl):
        ''' Constructor

        :param gllvl: Global Logging Level
        '''
        self._gllvl = gllvl

    def log(self, lvl, msg, raw=False, end='.\n'):
        ''' Print log message

        :param lvl: user-defined log level of message
        :param msg: message itself
        :param raw: flag to disable msg postformatting
        '''

        if lvl > self._gllvl or lvl < logLevel.CRITICAL:
            # invalid log level
            return

        prefix = '[%s%s%s]' % (logLevel.colour[lvl], logLevel.token[lvl],
                               colour.NORMAL)

        print(('' if raw else prefix) + msg),

    def encolour(self, clr, msg):
        ''' Colorize message

        :param clr: expected colour
        :param msg: user message
        :return: colorized text
        '''
        return clr + msg + colour.NORMAL