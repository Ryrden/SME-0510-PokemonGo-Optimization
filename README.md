# Pokemon Go Optimization

## **SME0510 - Introdução à Pesquisa Operacional**

### **Integrantes do grupo**

```text
Joel Felipe Coelho            - 4865826
João Lucas Pereira e Sousa    - 10994311
Moniely Silva Barboza         - 12563800
Ryan Souza Sá Teles           - 12822062  
```

## **O problema do treinador Pokémon**

Considere que um usuário do aplicativo Pokémon GO, estudante de Engenharia da Computação da USP, deseja coletar todos os 18 tipos de pokémons existentes, sendo eles, os que seguem: Aço, Água, Dragão, Elétrico, Fada, Fantasma, Fogo, Gelo, Inseto, Lutador, Normal, Pedra, Planta, Psíquico, Sombrio, Terrestre, Venenoso,  Voador. Convenientemente, existem 18 pontos focais no campus 1 e 2 da USP, onde cada um desses pontos possui pokémons de um tipo primário específico (ex: Tipo Fogo).
O mapeamento de tipos de pokémons, com seu respectivo ponto focal, é dado pela seguinte tabela:

| Ponto focal | Tipo Pokémon |
| ----------- | ------------ |
| A           | Aço          |
| B           | Água         |
| C           | Dragão       |
| D           | Elétrico     |
| E           | Fada         |
| F           | Fantasma     |
| G           | Fogo         |
| H           | Gelo         |
| I           | Inseto       |
| J           | Lutador      |
| K           | Normal       |
| L           | Pedra        |
| M           | Planta       |
| N           | Psíquico     |
| O           | Sombrio      |
| P           | Terrestre    |
| Q           | Venenoso     |
| R           | Voador       |

O mapeamento de pontos focais distribuídos nos campus 1 e 2 da USP, é dado pela seguinte imagem:

![Pontos focais distribuídos nos campus da USP de São Carlos](https://i.imgur.com/qmk5Sju.png)

*Imagem 1: Mapeamento dos pontos focais distribuídos nos campus da USP de São Carlos.*

Deixando claro que esse é um problema simétrico, isto é, a distância do percurso de A para B é equivalente à distância do percurso de B para A. Vale ressaltar que é necessário evitar a ida de um ponto xi para um mesmo ponto xi. Além disso, não está sendo considerada a distância real entre o campus 1 e o campus 2, apenas uma distância aparente.

Deixando claro que esse é um problema simétrico, isto é, a distância do percurso de A para B é equivalente à distância do percurso de B para A. Vale ressaltar que é necessário evitar a ida de um ponto xi para um mesmo ponto xi. Além disso, não está sendo considerada a distância real entre o campus 1 e o campus 2, apenas uma distância aparente.

Agora que foi introduzido o contexto do problema, focaremos no problema em si, e o que temos o objetivo de resolver. De forma resumida, o estudante do cenário gostaria de visitar todos esses 18 pontos focais (a fim de coletar cada tipo de pokémon existente) percorrendo a menor distância possível. Por exemplo, ele poderia começar do ponto B, ir para o A, C, D, F, E, e assim por diante. Essa configuração seria a mais performática possível? Além disso, também temos algumas restrições. Quando o estudante chega ao ponto focal H, em sequência, ele vai direto para o bandejão, que fica no ponto F. Logo depois, ele tem aula em um bloco próximo do ponto I, se reúne com amigos no ponto D, e parte para sua segunda aula no EESC, no ponto G. Por fim, finalizando as restrições, ele precisa em determinado momento, ele precisa se locomover para o CAMPUS 2, ele utiliza transporte público e pega o ônibus no ponto J e chega no ponto O, e sua aula acontece no ponto L. 

O treinador pokémon, poderia simplesmente observar a tabela descrita, e estudar o percurso mais rápido existente, todavia, existem (n − 1)! ordens em que os pontos focais poderiam ser visitados, logo este não é um problema que se pode resolver pela força bruta para qualquer valor razoável de n, especialmente no cenário em que n é 18, onde teríamos 355.687.428.096.000 possíveis percursos possíveis a serem percorridos. Vale ressaltar que no nosso cenário, em que há restrições de idas a pontos específicos a partir de uma origem especificada, a ordem de percursos seria significativamente menor, apesar de ainda ser grande o bastante para não ser factível um trabalho de força bruta.

## **Como rodar o projeto**

1. Baixe e instale [python](https://www.python.org/) em sua máquina
2. Instale as dependências: `pip install -r requirements.txt`
3. Rode  `python script.py` e seja feliz
