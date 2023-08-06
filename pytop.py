import os
import psutil

def listDirs():#listar os diretórios em /proc
    #array que armazena os diretórios de /proc
    sysDirs = [f for f in os.listdir('/proc') if f.isdigit()] #função da biblioteca os que lista o diretorio do caminho que recebe em seu parâmetro
    return sysDirs

def searchPath(userPath): #encontra todos os Processos gerados pelo binário
    dirs=listDirs()
    userPathPids=[]
    for pid in dirs:
        procsLinks=f"/proc/{pid}/exe"
        if os.path.exists(procsLinks) and os.path.islink(procsLinks):
            procPath=os.readlink(procsLinks)
            if userPath==procPath:
                userPathPids.append(pid)
    return userPathPids

def procMetrics(pid):
    try:
        process = psutil.Process(pid)
    except psutil.Error as e:
        print(e)
    else:
        # Porcentagem total de uso de CPU pelo processo
        cpu_percent = process.cpu_percent(interval=1)
        
        # Total de memória usada pelo processo em bytes
        mem_info = process.memory_info()
        mem_used = mem_info.rss
        
        # Total de atividade de disco pelo processo em bytes
        disk_usage = process.io_counters()

    
    return cpu_percent, mem_used, disk_usage

def showMetrics(pids):
    for pid in pids:
        cpu,mem,disk=procMetrics(int(pid))
        print(pid)
        print(cpu)#%
        print(mem)#bits
        print(disk)
        print('')

def main():
    binPath=input("bin: ")
    while True:
        binPids=searchPath(binPath)
        showMetrics(binPids)

main()