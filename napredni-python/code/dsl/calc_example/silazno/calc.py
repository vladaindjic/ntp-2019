"""
This is a variant of calc example using object processors for on-the-fly
evaluation.
"""
from __future__ import unicode_literals
import sys
from textx import metamodel_from_file

if sys.version < '3':
    text = unicode  # noqa
else:
    text = str

# Global variable namespace
namespace = {}


def expression_action(expression):
    ret = expression.operands[0]
    for operator, operand in zip(expression.operators,
                                 expression.operands[1:]):
        if operator == '+':
            ret += operand
        else:
            ret -= operand
    return ret


def term_action(term):
    ret = term.operands[0]
    for operator, operand in zip(term.operators,
                                 term.operands[1:]):
        if operator == '*':
            ret *= operand
        else:
            ret /= operand
    return ret


def factor_action(operand):
    if operand.op_num is not None:
        return operand.op_num
    elif operand.op_id:
        if operand.op_id in namespace:
            return namespace[operand.op_id]
        else:
            raise Exception('Unknown variable "{}" at position {}'
                            .format(operand.op_id, operand._tx_position))
    else:
        return operand.op_expr


def main(debug=False):
    processors = {
        'Expression': expression_action,
        'Term': term_action,
        'Factor': factor_action,
    }

    calc_mm = metamodel_from_file("calc.tx", auto_init_attributes=False,
                                 debug=debug)
    calc_mm.register_obj_processors(processors)

    input_expr = '''
        3 + 3 * 5
    '''

    expr = calc_mm.model_from_str(input_expr)
    result = expression_action(expr)
    print("Result is", result)


if __name__ == '__main__':
    main()
