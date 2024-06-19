import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def jacobi_method(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    iter_data = []
    
    for k in range(max_iter):
        x_new = np.zeros(n)
        
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        epsilon = np.linalg.norm(x_new - x, ord=np.inf)
        iter_data.append([k] + list(x_new) + [epsilon])
        
        if epsilon < tol:
            return x_new, k, iter_data
        
        x = x_new
    
    return x, max_iter, iter_data

def main():
    # Escolha do sistema
    system_type = int(input("Digite 2 para sistema 2x2 ou 3 para sistema 3x3: "))
    
    if system_type == 2:
        A = []
        b = []
        for i in range(2):
            row = list(map(float, input(f"Digite os coeficientes da linha {i+1} (separados por espaço): ").split()))
            A.append(row[:-1])
            b.append(row[-1])
        A = np.array(A)
        b = np.array(b)
        x0 = np.zeros(2)
        
    elif system_type == 3:
        A = []
        b = []
        for i in range(3):
            row = list(map(float, input(f"Digite os coeficientes da linha {i+1} (separados por espaço): ").split()))
            A.append(row[:-1])
            b.append(row[-1])
        A = np.array(A)
        b = np.array(b)
        x0 = np.zeros(3)
    
    else:
        print("Tipo de sistema inválido!")
        return
    
    # Parâmetros do método de Jacobi
    tol = 1e-4  # Ajuste da tolerância para 10^-4
    max_iter = 1000
    
    # Resolvendo o sistema
    sol, iterations, iter_data = jacobi_method(A, b, x0, tol, max_iter)
    print(f"Solução aproximada: {sol}, Iterações: {iterations}")

    # Tabela de iterações
    columns = ["Iteração"] + [f"x{i+1}" for i in range(len(x0))] + ["Epsilon"]
    iter_df = pd.DataFrame(iter_data, columns=columns)
    print(iter_df)
    
    # Plotando a tabela de iterações e a distância da solução exata
    fig, ax = plt.subplots(3, 1, figsize=(10, 12))
    for i in range(len(x0)):
        ax[0].plot(iter_df["Iteração"], iter_df[f"x{i+1}"], label=f'x{i+1}')
    ax[0].set_xlabel('Iteração')
    ax[0].set_ylabel('Valor')
    ax[0].legend()
    ax[0].grid(True)

    ax[1].plot(iter_df["Iteração"], iter_df["Epsilon"], label='Epsilon')
    ax[1].set_xlabel('Iteração')
    ax[1].set_ylabel('Erro')
    ax[1].legend()
    ax[1].grid(True)
    
    # Definindo a solução exata com base no sistema escolhido (para testes fornecidos)
    if system_type == 2:
        x_exact = np.array([1, -1])  # Exemplo para sistema 2x2, ajuste conforme necessário
    elif system_type == 3:
        x_exact = np.array([-1, 2, -3])  # Exemplo para sistema 3x3, ajuste conforme necessário
    
    distances = np.linalg.norm(iter_df.iloc[:, 1:len(x0)+1] - x_exact, axis=1)
    ax[2].plot(iter_df["Iteração"], distances, label='Distância da Solução Exata')
    ax[2].set_xlabel('Iteração')
    ax[2].set_ylabel('Distância')
    ax[2].legend()
    ax[2].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()