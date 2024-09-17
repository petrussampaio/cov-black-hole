# Simulação de Buracos Negros

Este projeto consiste em uma simulação de buracos negros, com foco na modelagem das composições físicas de um buraco negro. A implementação permite fornecer a massa do buraco negro como entrada e calcula propriedades astrofísicas com base nesse dado. O projeto também garante uma boa cobertura de código utilizando `pytest` e `coverage`.

## Descrição do Código

O código implementa funcionalidades relacionadas a buracos negros, incluindo o cálculo do raio de Schwarzschild e a densidade do buraco negro. A entrada principal é a massa do buraco negro, e o programa calcula as propriedades astrofísicas com base nessa massa.

### Principais Funcionalidades:

- **Cálculo do Raio de Schwarzschild**: Dado o valor da massa do buraco negro, o código calcula o raio de Schwarzschild, que é o limite esférico em torno de um buraco negro onde a gravidade é tão forte que nem mesmo a luz pode escapar.
  
- **Densidade do Buraco Negro**: O código calcula a densidade do buraco negro com base na massa fornecida.

- **Validação de Entradas**: O código valida a massa fornecida para garantir que seja um valor positivo e fisicamente plausível.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.10.12
- `pytest`
- `coverage`

Você pode instalar as dependências executando:

```bash
pip install pytest coverage
```

Pode executar os testes seguindo os passos:
```bash
coverage run -m pytest
```

Gerar relatório no terminal:
```bash
coverage report
```

Gerar relatório HTML:
```bash
coverage html
```
