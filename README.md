# PathTop

Este é um script Python que permite a busca por processos iniciados por um determinado binário e exibe algumas métricas de uso de CPU e memória para cada processo encontrado.
O script utiliza os módulos os, psutil e subprocess do Python. O módulo os é usado para listar os diretórios em /proc, o módulo psutil é usado para acessar dados de uso de CPU, memória e disco do processo.
Além de ser útil para monitorar métricas de processos em desenvolvimento, este código pode ser usado para monitorar processos em produção, desde que se tenha acesso ao caminho do binário que gerou os processos que se deseja monitorar. Essa abordagem é conveniente, pois não é necessário instalar softwares adicionais ou configurar ambientes complexos para monitorar os processos.
Para executar o script, basta salvar o código em um arquivo com a extensão .py e executar o comando python nome_do_arquivo.py no compilador de python. 
