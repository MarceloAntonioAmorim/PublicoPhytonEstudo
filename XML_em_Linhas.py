import os
import xml.dom.minidom

def abrir_xml_e_quebrar_linhas(nome_arquivo_entrada, nome_arquivo_saida):
    caminho_arquivo_entrada = os.path.join(os.path.dirname(__file__), nome_arquivo_entrada)

    # Abrir o arquivo XML
    with open(caminho_arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        conteudo_xml = arquivo.read()

    # Criar objeto DOM
    dom = xml.dom.minidom.parseString(conteudo_xml)

    # Adicionar quebras de linha por tag
    xml_formatado = dom.toprettyxml(indent='  ')

    # Salvar o XML com as quebras de linha
    caminho_arquivo_saida = os.path.join(os.path.dirname(__file__), nome_arquivo_saida)
    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write(xml_formatado)

if __name__ == "__main__":
    # Solicitar ao usuário o nome do arquivo de entrada
    arquivo_xml_entrada = input("Digite o nome do arquivo XML de entrada: ")

    # Solicitar ao usuário o nome do arquivo de saída
    arquivo_txt_saida = input("Digite o nome desejado para o arquivo XML de saída: ")

    abrir_xml_e_quebrar_linhas(arquivo_xml_entrada, arquivo_txt_saida)
