### README

# Implementação do Método de Jacobi

## Informações Gerais
**Matéria:** Cálculo Numérico  
**Universidade:** Universidade Federal do Tocantins (UFT)  
**Professor:** Rogério Azevedo Rocha  
**Nome:** Laura Barbosa Henrique
**Semestre:** 2024/1

## Descrição
Este projeto implementa o Método de Jacobi para a resolução numérica de sistemas de equações lineares. A implementação é feita em Python, utilizando bibliotecas como `numpy`, `pandas` e `matplotlib` para a manipulação de dados e visualização dos resultados.

## Requisitos
- Python 3.x
- Bibliotecas Python: `numpy`, `pandas`, `matplotlib`

Você pode instalar as bibliotecas necessárias utilizando o comando:
```bash
pip install numpy pandas matplotlib
```

## Estrutura do Código
O código está estruturado em duas partes principais: a função `jacobi_method` e a função `main`.

### Função `jacobi_method`
Esta função executa o Método de Jacobi para encontrar a solução aproximada de um sistema de equações lineares.

#### Parâmetros:
- `A`: Matriz dos coeficientes do sistema.
- `b`: Vetor dos termos independentes.
- `x0`: Vetor inicial de aproximação.
- `tol`: Tolerância para o critério de parada.
- `max_iter`: Número máximo de iterações permitidas.

#### Retornos:
- `x_new`: Solução aproximada.
- `k`: Número de iterações realizadas.
- `iter_data`: Dados das iterações para análise e plotagem.

### Função `main`
Esta função gerencia a entrada dos dados, chama a função `jacobi_method` e plota os resultados.

## Uso
1. Execute o script em um ambiente Python.
2. Escolha o tipo de sistema (2x2 ou 3x3) quando solicitado.
3. Insira os coeficientes do sistema e os termos independentes.
4. O programa calculará a solução aproximada utilizando o Método de Jacobi e apresentará os resultados.

### Exemplo de Uso
Ao executar o script, siga as instruções para entrada dos dados. Por exemplo, para um sistema 2x2, insira os coeficientes das equações e os termos independentes conforme solicitado.

## Resultados
O programa exibirá:
- A solução aproximada.
- O número de iterações realizadas.
- Uma tabela com os valores das iterações e os erros.
- Gráficos mostrando a evolução das soluções aproximadas, o erro em cada iteração e a distância da solução exata.

### Exemplo de Sistema

## Exemplo de Sistema
### Sistema 2x2
```
10x + 2y = 14
3x - y = 5
```

### Sistema 3x3
```
4x + y - z = 3
x + 3y + 2z = 15
2x - y + 4z = 8
```

### Saída Esperada
A solução aproximada, o número de iterações e os gráficos de convergência serão exibidos para o sistema inserido.

## Contribuições
Este projeto foi desenvolvido como parte da disciplina de Cálculo Numérico na Universidade Federal do Tocantins (UFT). Quaisquer contribuições ou sugestões são bem-vindas.

## Licença
Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais e acadêmicos.

---

**Laura Barbosa Henrique**  
Universidade Federal do Tocantins (UFT)  
Contato: laura.henrique@mail.uft.edu.br
