## Parser de dados
Sistema que importa lotes de arquivos .dat.
O sistema deve conseguir importar lotes de arquivo, ler, analisar e depois devolver um relatório dos dados coletados.
Há 3 tipos de dados diferentes no mesmo arquivo, para cada tipo há 1 layout diferente também.
- os itens são:
  - dados do vendedor
    - vendedor tem o id 001 e a linha tem o seguinte formato. 001çCPFçNameçSalary
  - dados do cliente
    - cliente tem o id 002 e a linha tem o seguinte formato. 002çCNPJçNameçBusinessArea
  - dados da venda
    - dados da venda tem o id 003 e a linha tem o seguinte formato. 003çSale IDç[Item ID-Item Quantity-Item Price]çSalesman name
    - dentro da linha de venda existe a linha de itens, que está envolta entre colchetes [].

### Dados de Exemplo

O seguinte é um exemplo dos dados que o sistema deve ser capaz de ler.
```
001ç1234567891234çPedroç50000
001ç3245678865434çPauloç40000.99
002ç2345675434544345çJose da SilvaçRural
002ç2345675433444345çEduardo PereiraçRural
003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çPedro
003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çPaulo
```
- O sistema deve ler somente arquivos .dat
- Após processar os arquivos no diretório padrão de entrada, para cada arquivo de entrada o sistema deve criar um arquivo dentro do diretório de saída padrão, que deve ser \<homepath\>/data/out.

- O conteúdo do arquivo de saída deve resumir os seguintes dados
  * Quantidade de clientes no arquivo de entrada
  * Quantidade de vendedor no arquivo de entrada
  * ID da venda mais cara
  * O pior vendedor

- O arquivo de saída padrão deve se chamar {flat_file_name}.done.dat;

# Setup
#### Requisitos mínimo:
> python > 3.6
#### Instalação

virtualenv
> python3 -m venv venv && source venv/bin/activate

Instale as libs necessárias
> pip install -r requirements.txt

Rode os testes
> python -m unittest -vv

Execute o código
> python source/main.py

A execução de main.py deve:
* criar a estrutura de diretórios ~/data/in, ~/data/out
* inserir o arquivo `example.dat` dentro do diretório de entrada da aplicação.
* gerar um arquivo `example.done.dat` no arquivo de saída
* monitorar modificações dentro do diretórios ~/data/in. Fique a vontade para adicionar novos arquivos.dat enquanto a aplicação roda.
