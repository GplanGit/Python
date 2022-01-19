#importa a biblioteca e instancia a planilha
from openpyxl import Workbook
wb=Workbook()

#instancia uma aba atica dentro da planilha
ws=wb.active

# Cria várias abas a planilha
ws1=wb.create_sheet("Mysheet")#insere no final das abas(default)
ws2=wb.create_sheet("Mysheet",0)#insere na primeira posição
ws3=wb.create_sheet("Mysheet",-1)# insere na penultima posição

#Mundando nome das planilhas
ws2.title="Mysheet_01"
ws3.title="Mysheet_02"

#Mudando cor das abas
ws.sheet_properties.tabcolor="1072BA"

#posicionando pelo nome da aba
#ws4=wb["New Title"]

#retorna nomes das abas
print(wb.sheetnames)

#retorna o nome das abas
for sheet in wb:
    print(sheet.title)
