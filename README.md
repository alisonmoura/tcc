## Setup

### Instalação de dependências

```
pip3 install -r requirements.txt
```

https://stackoverflow.com/questions/28863944/scikit-learn-typeerror-if-no-scoring-is-specified-the-estimator-passed-should

https://pypi.org/project/progress/

## Últimas Atualizações

### 2020.05.20-1
Corrigi a implementação do OSVM, estava fazendo o treinamento com dados positivos e o teste com todos os dados. Porém os resultados estavam superestimados, e a precisão só resultava em 100%. O problema estava na junção dos vetores pelo `np.concatenate`, o vetor estava separado em dois: os dados positivos e os dados negativos. O treinamento estava sendo feito corretamente com o vetor de dados positivos, e depois era feito a concatenação do vetor de dados negativos com os dados de teste (particionado pelo K-fold Cross Validation). Porém eu não estava "reatribuindo" o vetor concatenado (testes + negativos) no vetor de teste.