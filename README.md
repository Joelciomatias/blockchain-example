# Blockchain-exemplo

Um exemplo simples de uma blockchain em python

Fonte: https://www.udemy.com/course/formacao-engenheiro-de-blockchain/

## Instalação
#### Python 3.6.9


```bash
pip3 install -r requirements.txt
```

### Subir o programa:
```
python app.py

python app.py porta 

python app.py porta recebedor
```
porta para cada nó: 5000,5001,5002....

nome do recebeor padrão: mario, jose

### Minerar bloco
GET http://localhost:5000/mine-block HTTP/1.1

### Ver a blockchain
GET http://localhost:5000/get-blockchain HTTP/1.1

### Checar a blockchain
GET http://localhost:5000/blockchain-is-valid HTTP/1.1

### Restaurar a blockchain (copiar a blockchain de outros nos da rede)
GET http://localhost:5000/replace-chain HTTP/1.1

### Conecta um nó a outros nós da rede
POST http://localhost:5000/connect-node HTTP/1.1

{
    "nodes":[
        "http://localhost:5000",
        "http://localhost:5002"
        .....
    ]
}

### Adiciona uma transação ao bloco atual
POST http://localhost:5000/add-transaction HTTP/1.1

{
    "sender":"Fernando",
    "receiver":"Pedro",
    "amount": 100
}
