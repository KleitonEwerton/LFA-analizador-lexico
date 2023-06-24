# Analizador Lexíco
No âmbito da disciplina de Linguagens Formais e Autômatos (LFA), foi desenvolvido um projeto com o objetivo de criar um analisador léxico para diversas funcionalidades. O projeto foi concebido e implementado pelos alunos Kleiton e Arthur.

O projeto teve como propósito desenvolver um analisador léxico capaz de reconhecer e classificar corretamente os tokens presentes no código fonte. Para isso, foram aplicados conceitos e técnicas estudados na disciplina LFA, como a definição de gramáticas regulares, a construção de autômatos finitos determinísticos (AFDs) e a utilização de expressões regulares para o reconhecimento dos padrões léxicos.


<h2>Instalação e execução</h2>

Instalando as dependências
````
pip install -r requirements.txt
````

Executando projeto
````
python3 main.py ./analisador-definicoes.json ./analisador-strings.json
````
<h2>Observações</h2>

[X] Ler arquivos de definições do Automato

    O arquivo 'analisador-definicoes.json' exemplifica a forma como o AFD deve ser definido para realizar as análises.;

    Observação: O atributo "endLine" define o caractere delimitador para análise, no entanto, é necessário adicionar essa transição no escopo de transições do autômato de forma apropriada.
    

[x] Ler arquivo para análise

    O arquivo 'analisador-strings.json' exemplifica a forma como os textos a serem analisados devem ser passados.

    Observação: É importante ressaltar que não é necessário adicionar o marcador "endLine" na string analisada. Caso esse marcador seja inserido indevidamente na string, erros podem ocorrer durante a análise léxica. O marcador "endLine" deve ser utilizado apenas na definição do analisador léxico, especificando o caractere delimitador para a análise correta dos tokens.
