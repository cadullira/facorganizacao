# Projeto de Banco de Dados

## Banco de Dados: SQLite3

### Comandos

**Instalação no Linux**

    sudo apt update
    sudo apt install sqlite3

**Ajuda**

    .help

**Sair do Terminal do SQLite3**

    .quit
    .help

**Criar Base de Dados**
*Genérica*

    sqlite3 NomeDaBaseDeDados.db
*Versão SQLite3*

    sqlite3 NomeDaBaseDeDados.db3
**Visualizar Base de Dados**

    .databases

**Abrir uma Base de Dados**

    .open NomeDaBaseDeDados


**Visualizar Tabelas de uma Base de Dados**

    .tables
**Criar tabela**

    create table NomeDaTabela(atributo1 tipoDeDado [regras], atributo2 tipoDeDado [regras]);

**Regras**

    NOT NULL
    UNIQUE
    PRIMARY KEY
    FOREIGN KEY
    CHECK
    DEFAULT
    CREATE INDEX
    
    
### Nomenclaturas e boas práticas

 - Nome tabela (entidade) no plural, ex: funcionarios
 - Comando SQL em maiúsculo, ex: `CREATE TABLE nomeDaTabela(atribtuto1 VARCHAR(10) NOT NULL, atributo2 INT NOT NULL)`;
 - `PRAGMA foreign_keys = ON;` comando do SQLite3 para que se possa realizar mudanças em cascata em tabelas que tenham ligações através  de foreign key
 - `DROP TABLE nomeDaTabela;` comando para excluir determinada tabela da base de dados.
 - `DELETE FROM nomeDaTabela WHERE atributo = 'algumaCoisa';`
