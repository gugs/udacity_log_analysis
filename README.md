Capítulo - Análise de Log
=============

Este projeto diz respeito ao capítulo análise de log do curso de desenvolvimento fullstack nanodegree da udacity. 

Visando atender aos requisitos do projeto do referido capítulo, o script contido na pasta Project - Python File resolve a análise de log do dump da base de dados fornecido. 

Para executar esse arquivo, tenha instalado a versão 3 do python. Como estabelecido no projeto, não há necessidade de entradas por parte do usuário. 

Quais são as saídas do script
==============

A análise do log tem como base verificar:

1) Os 3 artigos mais lidos da base são exibidos com a respectiva quantidade de visualizações.

2) Quem são os autores mais lidos.

3) Exibir a quantidade de requisições malsucedidas com base nas respostas HTTP registradas no log.

Preparação do Ambiente
==============

1) Use um terminal para rodar este programa. Caso seu sistema operacional seja baseado em Unix, uso o próprio terminal do Unix no seu computador. No Windows, nós recomendamos usar o terminal Git Bash que vem com o software Git. Se você não tiver o Git instalado, baixe o Git do git-scm.com.

2) Instale o VirtualBox. VirtualBox é o software que na verdade executa a máquina virtual. Você pode baixá-lo no virtualbox.org, aqui. Instale o plataform package para seu sistema operacional. Você não precisa do pacote de extensão ou do SDK. Você não precisa iniciar o VirtualBox após instalá-lo. O próximo programa a ser instalado, o Vagrant, vai fazer isso.

Usuários Ubuntu: Se você estiver executando Ubuuntu 14.04 instale o VirtualBox usando o Ubuntu Software Center em vez disso. Devido a um bug reportado, instalar o VirtualBox a partir do site pode desinstalar outros softwares que você precisa.

3) Instale o Vagrant. Vargrant é o software que configura a VM e permite que você compartilhe arquivos entre seu computador host e o sistema de arquivos da VM. Baixe no vagrantup.com. Instale a versão de seu sistema operacional.

Usuários Windows: O instalador pode lhe pedir para dar permissões de rede ao Vagrant ou para fazer uma exceção no firewall. Certifique-se de permitir isto.

4) Download e configuração da VM. Você pode baixar e extrair este arquivo: https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip

Isso lhe dará um diretório chamado FSND-Virtual-Machine. Ele pode ser localizado dentro de sua pasta de Downloads, ou no local selecionado para download.

Como alternativa, você pode usar o Github para copiar e clonar o repositório https://github.com/udacity/fullstack-nanodegree-vm.

De qualquer forma, você vai acabar com um novo diretório contendo os arquivos da VM. Mude para este diretório no seu terminal com cd. Dentro, você encontrará outro diretório chamado vagrant. Altere o diretório para o diretório vagrant.

5) Iniciando a máquina virtual. De seu terminal, dentro do subdiretório vagrant, execute o comando vagrant up. Isso fará com que Vagrant baixe o sistema operacional Linux e instale. Isto pode demorar um pouco (muitos minutos) dependendo do quão rápida é sua conexão de Internet. Quando vagrant up terminar de executar, você terá eu shell prompt de volta. Neste ponto, você pode executar vagrant ssh para logar eu seu Linux VM recentemente instalado!

6) Executando o banco de dados. O servidor de banco de dados PostgreSQL será automaticamente iniciado dentro da VM. Você pode usar a ferramenta de linha de comando psql para acessar e executar declarações SQL. Para logar e deslogar, se você digitar exit (ou Ctrl-D) no prompt shell dentro da VM,você será deslogado(a), e colocado(a) de volta na shell de seu computador host. Para voltar a logar, certifique-se de que você está no mesmo diretório e digite vagrant ssh novamente.

Se você reiniciar seu computador, você precisará executar vagrant up para reiniciar a VM.

Resolução de Problemas
==============

Não sei se funcionou:

Se você consegue digitar vagrant ssh e logar à sua VM, então funcionou! É normal que o processo de vagrant up exiba um monte de texto em muitas cores, incluindo às vezes mensagens assustadoras em vermelho, verde e roxo. Se você voltar ao seu shell prompt no final, e você puder logar, então está tudo OK.

vagrant up está demorando muito. Por que?

Porque está baixando um sistema operacional Linux inteiro da Internet.

Estou no Windows e recebendo um erro sobre virtualização:

Às vezes, outros programas de virtualização como Docker ou Hyper-V podem interferir com o VirtualBox. Tente fechar estes outros programas primeiro.

Além disso, alguns PCs Windows têm configurações no BIOS ou UEFI (firmware) ou no sistema operacional que desabilitam o uso de virtualização. Para alterar isso, você pode precisar reiniciar o computador e acessar as configurações de firmware. Uma pesquisa na web pode ajudá-lo(a) a encontrar as configurações para seu computador e sistema operacional. Infelizmente, existem tantas versões diferentes de Windows e PCs que não podemos oferecer um guia simples para fazer isto.

Por que estamos usando uma VM? Parece complicado!

É complicado. Neste caso, o motivo é ser capaz de oferecer o mesmo software (Linux e PostgreSQL) independentemente do tipo de computador você está usando.

Recebi uma mensagem de erro, o que fazer?

Se você está recebendo uma mensagem de erro textual específica, tente a procurar no seu site buscas favorito. Se isso não ajudar, tire um screenshot e poste nos fóruns de discussão, juntamente com tantos detalhes quanto você puder fornecer sobre o processo passou para chegar nela.

Informações do Banco de Dados
==============

SGDB: Postgres

Nome da Base: news

Tabelas: Authors
         Articles
         Log

