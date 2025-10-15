from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Mapeamento do nome enviado para o nome esperado
field_map = {
    "Id": "id",
    "Nome": "nome",
    "Data Inicial": "dataInicial",
    "Data final": "dataFinal",
    "Prioridade": "prioridade",
    "Sobre": "sobre"
}

@app.route('/upload-json', methods=['POST'])
def upload_json():
    if 'file' not in request.files:
        return jsonify({'erro': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'erro': 'Nome de arquivo vazio'}), 400

    if not file.filename.endswith('.json'):
        return jsonify({'erro': 'Arquivo deve ser .json'}), 400

    try:
        data = json.load(file)

        # Verifica se é uma lista
        if not isinstance(data, list):
            return jsonify({'erro': 'JSON deve ser uma lista de objetos'}), 400

        tarefas_normalizadas = []

        for tarefa in data:
            nova_tarefa = {}
            for key_original, key_normalizado in field_map.items():
                if key_original not in tarefa:
                    return jsonify({'erro': f'Campo ausente: {key_original}'}), 400
                nova_tarefa[key_normalizado] = tarefa[key_original]

            tarefas_normalizadas.append(nova_tarefa)
        #print(f'teste--:{tarefas_normalizadas}')
        return jsonify({'mensagem': 'JSON recebido com sucesso', 'dados': tarefas_normalizadas}), 200

    except json.JSONDecodeError:
        return jsonify({'erro': 'Erro ao decodificar o JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)


#rodar o arquivo e depois usar o powershell
#curl.exe -X POST http://localhost:5000/upload-json -F "file=@Task.json"
