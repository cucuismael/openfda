import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Biofisica',
    'Curso': 'Primero',
    'titulacion': 'Ingenieria Biomedica',
    'Temas' : [{
        'Numero': '1',
            'Titulo' : 'Campo electrico',
            'Horas' : '12',
        },
        {'Numero' : '2',
            'Titulo' : 'Ley de Gauss',
            'Horas' : '16',
        }
    ]
})


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
