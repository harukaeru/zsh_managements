EXPORT_G3 = 'export {}=$g3;\n'
g3_aliases = [
    'ge3',
    'gE3',
    'g23',
    'g2',
    'G3'
]

ZKERO_LINES = (EXPORT_G3.format(a) for a in g3_aliases)
