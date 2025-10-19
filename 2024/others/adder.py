from graphviz import Digraph

# Create a 1-bit full adder diagram
dot = Digraph(comment='1-bit Full Adder')

# Add input nodes
dot.node('A', 'A (input 1)')
dot.node('B', 'B (input 2)')
dot.node('Cin', 'Carry in')

# Add gate nodes
dot.node('XOR1', 'XOR')
dot.node('XOR2', 'XOR')
dot.node('AND1', 'AND')
dot.node('AND2', 'AND')
dot.node('OR', 'OR')

# Add output nodes
dot.node('Sum', 'Sum')
dot.node('Cout', 'Carry out')

# Add edges
dot.edge('A', 'XOR1')
dot.edge('B', 'XOR1')
dot.edge('XOR1', 'XOR2')
dot.edge('Cin', 'XOR2')
dot.edge('XOR2', 'Sum')

dot.edge('A', 'AND1')
dot.edge('B', 'AND1')
dot.edge('XOR1', 'AND2')
dot.edge('Cin', 'AND2')

dot.edge('AND1', 'OR')
dot.edge('AND2', 'OR')
dot.edge('OR', 'Cout')

dot.render('full_adder', format='pdf', view=True)