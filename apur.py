import requests
import time
import csv
from datetime import datetime
from jsonpath_rw import parse
import gui


lulaAtual = 0
bolsoAtual = 0
bolsoDif = 0
lulaDif = 0
total = 155756933
gui.hellogui()

while(True):
    req = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')
    if(req.status_code == 200):
        respJson = req.json()

        
        now = datetime.now()
        print(str(now) + ' ####################################################')

        percent = parse('$.pst')
        perc = percent.find(respJson)
        print(str(perc[0].value) + ' % de urnas apuradas')


        bVotosJson = parse('$.cand[1].vap')
        bolso = bVotosJson.find(respJson)
        bPercentJson = parse('$.cand[1].pvap')
        bolsoP = bPercentJson.find(respJson)
        nomeJson = parse('$.cand[1].nm')
        nome1 = nomeJson.find(respJson)


        bolsoAnterior = float(bolsoP[0].value.replace(',','.'))


        if(bolsoAtual != bolsoAnterior):
            print("""
            
            
            
            """)
            print('MUDANÇA:')

            bolsoDif = bolsoAnterior - bolsoAtual
            bolsoAtual = bolsoAnterior

        

        print(nome1[0].value + ' ' + str(bolso[0].value) + ' votos || ' + str(bolsoP[0].value) + ' %     Dif(%): ' + str(bolsoDif))



        lVotosJson = parse('$.cand[0].vap')
        lula = lVotosJson.find(respJson)
        lPercentJson = parse('$.cand[0].pvap')
        lulaP = lPercentJson.find(respJson)
        nomeJson = parse('$.cand[0].nm')
        nome2 = nomeJson.find(respJson)

        lulaAnterior = float(lulaP[0].value.replace(',','.'))

        if(lulaAtual != lulaAnterior):

            print('MUDANÇA: ################################################')

            
            lulaDif = lulaAnterior - lulaAtual
            lulaAtual = lulaAnterior
        



        print(nome2[0].value + ' ' + str(lula[0].value) + ' votos || ' + str(lulaP[0].value) + ' %     Dif(%): ' + str(lulaDif))
        dif = lulaAtual - bolsoAtual
        fields = [datetime.now(), perc[0].value, dif, nome1[0].value, nome2[0].value, bolso[0].value, lula[0].value, bolsoP[0].value, lulaP[0].value, bolsoDif, lulaDif]
        with open(r'apuracao.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
        print('Diferença: ' + str(lulaAtual - bolsoAtual))

        if((int(bolso[0].value) - int(lula[0].value)) > (total - (int(bolso[0].value) + int(lula[0].value)))):
            while(True):
                print(nome2[0].value + '   VENCEUU!!')
        

        time.sleep(10)

