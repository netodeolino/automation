# -*- coding: utf-8 -*-
import os
import zipfile
import shutil

def moverArquivos(oldPath, newPath):
  lista = os.listdir(oldPath) #lista separando apenas os arquivos do caminho.

  if(not os.path.exists(dir)):    
    os.mkdir(dir)

  # *** lista_len recebe o tamanho da lista ***
  lista_len = len(lista)

  x = 0
  # *** Utilizar a variável ao invés de chamar 'os.listdir()' ***
  while x < lista_len:
    caminhoCompleto_old = oldPath + lista[x] #variável recebe caminho + arquivo, conforme indice
    caminhoCompleto_new = newPath + lista[x] #variável recebe caminho + arquivo, conforme indice
    shutil.move(caminhoCompleto_old, caminhoCompleto_new) #módulo 'shutil.move()' move os arquivos
    print(x, '-', lista[x]) #apenas para ver como está sendo feito
    x += 1

def gerarZip(oldPath, zip):
  fantasy_zip = zipfile.ZipFile(zip, 'w')

  for folder, subfolders, files in os.walk(oldPath):
    for file in files:
      fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), oldPath), compress_type = zipfile.ZIP_DEFLATED)

  fantasy_zip.close()
  print("Arquivo zipado com sucesso : {}".format(zip))

def main(path, oldPath, newPath, zip):
  if(os.path.exists(path)):
    gerarZip(oldPath, zip)
  else:
    moverArquivos(oldPath, newPath)
    gerarZip(oldPath, zip)

if __name__ == "__main__":
  #main("path-da-pasta-para-zipar", "pasta-origem", "pasta-destino", "path-e-nome-do-zip")
  main("./files", "./files", "./files", "files.zip")