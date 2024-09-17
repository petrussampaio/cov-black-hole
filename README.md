# Simulação de Buracos Negros

Este projeto consiste em uma simulação de buracos negros, com foco na modelagem das composições físicas de um buraco negro. A implementação permite fornecer parâmetros físicos específicos para calcular propriedades do buraco negro, testar a consistência desses cálculos e garantir uma boa cobertura de código utilizando `pytest` e `coverage`.

## Descrição do Código

O código implementa funcionalidades relacionadas a buracos negros, como o cálculo de massa, raio de Schwarzschild, e outros parâmetros astrofísicos. Os usuários podem fornecer entradas, como massa e densidade, e o programa calculará as propriedades do buraco negro com base nesses dados.

### Principais Funcionalidades:

- **Cálculo do Raio de Schwarzschild**: Dado um valor de massa, o código calcula o raio de Schwarzschild, que é o limite esférico em torno de um buraco negro onde a gravidade é tão forte que nem mesmo a luz pode escapar.
  
- **Densidade do Buraco Negro**: O código também calcula a densidade do buraco negro, permitindo inferir propriedades físicas adicionais com base nas entradas fornecidas.

- **Validação de Entradas**: O código valida as entradas fornecidas para garantir que sejam fisicamente plausíveis, como uma massa positiva e uma densidade compatível com os modelos de buracos negros.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.x
- `pytest`
- `coverage`

Você pode instalar as dependências executando:

```bash
pip install pytest coverage
