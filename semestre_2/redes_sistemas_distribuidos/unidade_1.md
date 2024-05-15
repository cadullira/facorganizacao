# Conceitos básicos de Redes de Computadores e Sistemas Distribuídos
## Escopo de uma rede

LAN (*Local Area Network*) -> rede abrangência limitada
10 km
ponto a ponto e cliente-servidor
host - servidor

MAN (*Metropolitan Area Network*) -> Bairros e até cidades inteiras

WAN (Wide Area Network) -> Grande abrangência, exemplo: internet

Internet uma rede de redes

ISO (*International Organization for Standartization*) cria um modelo referência O **Modelo OSI** (Open Systems Interconnect)  criado em 1984, é um conjunto de padrões que garantiram maior compatibilidade e interoperabilidade entre os vários tipos de tecnologias de rede, criados por várias empresas de todo o mundo.

Possui 7 camadas:

 - Aplicação
 - Apresentação
 - Sessão
 - Transporte
 - Rede
 - Enlace
 - Física

**Modelo TCP/IP** (*Transmission Control Protocol/Internet Protoco*l) - ARPANET patrocinada pela Defesa dos Estados Unidos

Possui 4 camadas:

 - Aplicação
 - Transporte
 - Internet
 - Acesso à Rede

**TCP/IP** mais compacto que o **OSI**, uniu camadas

|TCP/IP| OSI   | Serviços e Funções
|------------|-----------------|----------
|  Aplicação          | **7. Aplicação 6. Apresentação 5. Sessão**| **7.** Mais próxima dos usuários. Exemplo: Navegador de internet, gerenciador de e-mail, compartilhamento de arquivos, serviços de DNS. **6.** Faz a conversão de vários formatos de dados usando um formato comum. **5.** Estabelece, gerencia e termina sessões entre dois hosts que se comunicam. A camada de sessão fornece seus serviços à camada de apresentação. Ela também sincroniza o diálogo entre as camadas de apresentação dos dois hosts e gerencia a troca de dados entre eles.
|  Transporte         | **4. Transporte**											 | **4.** Segmenta os dados do sistema host que está enviando e monta os dados novamente em uma seqüência de dados no sistema host que está recebendo.  
|  Internet           | **3. Rede**														 | **3.** Seleciona os de caminhos, roteamento e endereçamento
|  Acesso à Rede      | **2. Enlace** e **1. Física**									 |    **2.** Trata do endereçamento físico (em oposição ao endereçamento lógico), da topologia de rede, do acesso à rede, da notificação de erro, da entrega ordenada de quadros e do controle de fluxo. **1.** Define as especificações elétricas, mecânicas, funcionais e de procedimentos para ativar, manter e
desativar o link físico entre sistemas finais.

**HTTP – HyperText Transfer Protocol** ou *Protocolo de Transferência de Hipertexto.*

**FTP – File Transfer Protocol** ou *Protocolo de Transferência de
Arquivos.*

**SMTP – Simple Mail Transfer Protocol** ou *Protocolo de Transferência de Correio Simples.*

**POP3 – Post Office Protocol versão 3** 

Enviar um e-mail: **Cliente (host - remetente)** -> **Servidor de Email (SMTP)** -> **Servidor de Email (SMTP)** -> **Cliente (host - destinatário)** -> "E-mail chegou" -> **POP3** entra em ação, responsável por dá ao Cliente visualizar as mensagens trocadas no protocolo **SMTP**. No POP3 possui três etapas: autorização, transação, atualização.

N° HOST = CPF

**DNS – *Domain Name System** - *Sistema de Nomes de Domínio*, mapear /traduzir os números para um nome fácil de ser decorado e digitado.

> Os sistemas **proprietários** têm desenvolvimento, posse e controle
> privados. Na indústria de computadores, proprietário é o contrário de
> **aberto**. Proprietário significa que uma empresa ou um pequeno grupo de
> empresas controla todos os usos da tecnologia. "Aberto" quer dizer que
> o livre uso da tecnologia está disponível para o público.


