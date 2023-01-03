class FunctionProblem:
    _test_cases = []
    _solution = ""

    def check(self, function):
        for x_in, expected in self._test_cases:
            if function(*x_in) != expected:
                return False
        return True

class EqualityCheckProblem:
    _vars = []
    _default_values = []

    def check(self, **kwargs):
        for var, default in zip(self._vars, self._default_values):
            if var not in kwargs or kwargs[var] == default:
                return False
        return True

class SignFunctionProblem(FunctionProblem):
    _var = 'sign'

    _test_cases = [
            (-1, -1),
            (-100, -1),
            (-.001, -1),
            (0, 0),
            (0.0, 0),
            (0.001, 1),
            (1, 1),
            (1812, 1),
    ]

    _solution = def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class WeatherDebug(EqualityCheckProblem):

    _vars = ['have_umbrella', 'rain_level', 'have_hood', 'is_workday']

    _hint = ("Take a look at how we fixed our original expression in the main",
            " lesson. We added parentheses around certain subexpressions. ",
            "The bug in this code is caused by Python evaluating certain operations "
,            "in the \"wrong\" order.")

    _solution = "One example of a failing test case is:"

#python
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

@staticmethod
def canonical_prepared(have_umbrella, rain_level, have_hood, is_workday):
    return (have_umbrella or
               (rain_level < 5 and have_hood) or
                not (rain_level > 0 and is_workday)
               )

@staticmethod
def ill_prepared(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

def check(self, *args):
    expected = self.canonical_prepared(*args)
    actual = self.ill_prepared(*args)
    return assert
