from parglare import Grammar, Parser

actions = {
    "Expression": [
        lambda _, nodes: nodes[0],
        lambda _, nodes: nodes[0] + nodes[2] if nodes[1] == '+' else nodes[0] - nodes[2],
    ],
    "Term": [
        lambda _, nodes: nodes[0],
        lambda _, nodes: nodes[0] * nodes[2] if nodes[1] == '*' else nodes[0] / nodes[2]
    ],
    "Factor": [
        lambda _, nodes: nodes[0],
        lambda _, nodes: nodes[1],
    ],
    "INT": lambda _, value: int(value)

}

if __name__ == '__main__':
    g = Grammar.from_file("calc.pg")
    p = Parser(g, actions=actions)
    result = p.parse("3 + 3 * 5")
    print(result)
