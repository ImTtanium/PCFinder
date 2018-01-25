import easygui as ei
import webbrowser as webb

title = "PC Finder"
msg = "Escolha o tipo de computador que esta procurando"
perfis = ["PC GAMER", "ESCOLA/ESCRITÓRIO", "DOMÉSTICO", "EDIÇÃO PROFISSIONAL"]

escolha = ei.choicebox(msg, title, perfis)

if escolha == perfis[0]:
    title = "PC Finder"
    msg = "Esoolha a faixa de valor que esta disposto a pagar"
    perfis = ["2.500 a 4.000" , "4.000 a 5.500", "5.500 a 7.000"]
    title1 = 'Computador ideal'
    msg1 = "Informe qual relação de marcas você deseja? (Processador/Placa de Video)"
    variacoes_opcoes = ['Intel/NVIDIA', 'Intel/AMD', 'AMD/NVIDIA', 'AMD/AMD']

    valor = ei.choicebox(msg, title, perfis)
    variacao = ei.choicebox(msg1, title, variacoes_opcoes)

    if valor == "2.500 a 4.000":
        if variacao == 'Intel/NVIDIA':
            msg= ' Processador: i5 7400 3.0Ghz 6Mb \n Placa de Video: GeForce GTX 1060 3Gb\n' \
                   'Memoria Ram: 8Gb DDR4 \n Disco Rigido: 1Tb\n\n Preço: R$3.157,93 \n\n Acessar o link do PC proposto?'
            yn= ei.ynbox(msg, title1, choices=['Sim','Não'])
            if yn == 1:
                webb.open('https://www.terabyteshop.com.br/produto/6882/PC-Gamer-T-Soldier-LVL-2-Intel-Placa-de-Video-Memoria-HD-Fonte-Gabinete')
            else:
                exit()
        if variacao == 'Intel/AMD':
            msg='Processador:Intel i3-7100 3.9 Ghz 6Mb 7ª Geração  \n Placa de Video: Radeon  RX 550 2Gb \n' \
                   'Memoria ram: 8Gb DDR4 \n Dico rigido: 1Tb \n\n Preço: R$2.450,50 \n\n Acessar o link do PC proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn == 1:
                webb.open('https://www.pichau.com.br/computadores/pichau-gamer/computador-pichau-gamer-i3-7100-amd-radeon-rx-550-2gb-8gb-hd-1tb-400w-mt-g600bk')
            else:
                exit()
        if variacao == 'AMD/AMD':
            msg= 'Processador: AMD FX-8300 3.3Ghz 8Mb \n Placa de Video: Radeon RX 570 4Gb \n'\
                  'Memoria ram: 8Gb DDR3 \n Disco rigido: 1Tb \n\n Preço: R$3.149,80 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.pichau.com.br/computadores/pichau-gamer/computador-pichau-gamer-fx-8300-redeon-rx-570-4gb-8gb-hd-1tb-400w-si-5100')
            else:
                exit()
        if variacao == 'AMD/NVIDIA':
            msg= 'Processador: Ryzen 5 1500X 3.7GHZ 16Mb \n Placa de Video: GeForce GTX 1060 6Gb \n'\
                  'Memoria ram: 8Gb DDR4 \n Disco rigido: 1Tb \n\n Preço: R$3.613,98 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.terabyteshop.com.br/produto/8027/PC-Gamer-T-COMMANDER-LVL-2-AMD-Ryzen-5-1500x-Placa-de-Video-Nvidia-GeForce')
            else:
                exit()
    if valor == "4.000 a 5.500":
        if variacao == 'Intel/NVIDIA':
            msg= 'Processador: i5 7600 3.5GHZ 7ª Geração 6Mb \n Placa de Video: GeForce GTX 1070 TI 8Gb \n'\
                  'Memoria ram: 16Gb DDR4 \n Disco rigido: 1Tb \n\n Preço: R$5.494,75 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.terabyteshop.com.br/produto/6909/PC-Gamer-T-Captain-LVL-3-Intel-Placa-de-Video-Memoria-HD-Fonte-Gabinete')
            else:
                exit()
        if variacao == 'Intel/AMD':
            msg= 'Processador: Intel i7-7700 4.2Ghz 6Mb 7ª Geração\n Placa de Video: Radeon RX 580 8Gb \n'\
                  'Memoria ram: 8Gb DDR4 \n Disco rigido: 1Tb \n\n Preço: R$4.534,67 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.pichau.com.br/computadores/pichau-gamer/computador-pichau-gamer-i7-7700-xfx-radeon-rx-580-gts-8gb-8gb-ddr4-hd-1tb-500w-spec-03')
            else:
                exit()
        if variacao == 'AMD/NVIDIA':
            msg= 'Processador:AMD Ryzen 5 1600 3.6GHz 16Mb \n Placa de Video: GeForce GTX 1070 TI Strix OC 8Gb \n'\
                  'Memoria ram: 16Gb DDR4 \n Disco rigido: 1Tb \n\n Preço: R$5.286,99 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.terabyteshop.com.br/produto/8010/PC-Gamer-T-Captain-LVL-3-AMD-Ryzen-5-1600-Placa-de-Video-Nvidia-GeForce')
            else:
                exit()
        if variacao == 'AMD/AMD':
            msg= 'Processador: \n Placa de Video: \n'\
                  'Memoria ram: Gb DDR4 \n Disco rigido: Tb \n\n Preço: \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open()
            else:
                exit()
    if valor == "5.500 a 7.000":
        if variacao == 'Intel/NVIDIA':
            msg= 'Processador: Intel i7 8700K 3.7 GHZ 8ª Geração \n Placa de Video: GeForce GTX 1070 TI 8GB \n'\
                  'Memoria ram: 16Gb DDR4 \n Disco rigido: 1Tb \n\n Preço: R$6.572,68 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.terabyteshop.com.br/produto/8486/PC-Gamer-T-Power-General-LVL-3-8-gen-Intel-Placa-de-Video-Memoria-HD-Fonte-Gabinete')
            else:
                exit()
        if variacao == 'Intel/AMD':
            msg= 'Esta configuração não atinge o valor mínimo requerido. O computador mais caro nesta configuração é:\n\n' \
                 'Processador:Intel i5-7400 3.5Ghz 6Mb 7ª geração \n Placa de Video: Radeon RX 580 8Gb\n'\
                  'Memoria ram: 8Gb DDR4 \n Disco rigido: 1Tb \n\n Preço: R$4.190,50 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.pichau.com.br/computadores/pichau-gamer/computador-pichau-gamer-i5-7400-xfx-radeon-rx-580-gts-8gb-8gb-ddr4-hd-1tb-500w-spec-03')
            else:
                exit()
        if variacao == 'AMD/NVIDIA':
            msg= 'Processador:  AMD Ryzen 7 1700X 3.8Ghz 20Mb \n Placa de Video: GeForce MSI GTX 1080 8GB\n'\
                  'Memoria ram: 16Gb DDR4 \n Disco rigido: 1Tb hibrid \n\n Preço: R$ 6.422,25 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.terabyteshop.com.br/produto/8122/PC-Gamer-T-Power-Warlord-LVL-3-AMD-Ryzen-Placa-de-Video-Memoria-HD-Fonte-Gabinete')
            else:
                exit()
        if variacao == 'AMD/AMD':
            msg= 'Processador: AMD Ryzen 7 1700X 3.8GHZ 20MB\n Placa de Video: GeForce MSI GTX 1080 8GB OC Armor \n'\
                  'Memoria ram: 16Gb DDR4 \n Disco rigido: 1Tb \n\n Preço: R$ 6.422,25 \n\n Acessar o link do PC Proposto?'
            yn= ei.ynbox(msg,title1, choices=['Sim','Não'])
            if yn ==1:
                webb.open('https://www.terabyteshop.com.br/produto/8122/PC-Gamer-T-Power-Warlord-LVL-3-AMD-Ryzen-Placa-de-Video-Memoria-HD-Fonte-Gabinete')
            else:
                exit()


if escolha == perfis[1]:
    valores = ["1.500 a 2.300", "2.300 a 3.000"]
    valor = ei.choicebox("Esoolha a faixa de valor que esta disposto a pagar",
                             "PC Finder",
                             valores)

    variacoes = ["Notebook", "Computador"]
    variacao = ei.choicebox("Escolha seu modelo de preferência:",
                            "Computador ideal",
                            variacoes)

    if valor == "1.500 a 2.300"  :
        if variacao == "Notebook":
            msg = ' Processador: i3 6100 2.3Ghz 3MB \n' \
                  ' Memoria Ram: 4Gb DDR4 \n Disco Rigido: 500Gb\n\n Preço: R$1.929,95 \n Acessar o link do PC proposto?'
            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.pichau.com.br/notebooks/notebooks/notebook-lenovo-v310-14isk-intel-i3-6100u-4gb-hdd-500gb-14-polegadas-windows-10-home-80uf0000br')
            else:
                exit()

        if variacao == variacoes[1]:
            msg = ' Processador: FX-6300 3.5 Ghz 8MB \n' \
                  ' Memoria Ram: 4Gb DDR3 \n Disco Rigido: 1 Tb\n\n Preço: R$1.499,88 \n Acessar o link do PC proposto?'
            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.pichau.com.br/computadores/pichau-home/computador-pichau-home-express-fx-6300-4gb-1tb-wisecase-monitor-21-5-led-full-hd')
            else:
                exit()

    if valor == valores[1]:
        if variacao == variacoes[0]:
            msg = ' Processador: i5 7200U 2.5Ghz 3MB \n' \
                  ' Memoria Ram: 8Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$2.899,07 \n Acessar o link do PC proposto?'
            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.pichau.com.br/notebooks/notebooks/notebook-vaio-fit-i5-7200u-8gb-memoria-hd-1tb-15-6-pol-windows-10-home-vjf155f11x-b0411b')
            else:
                exit()
        if variacao == variacoes[1]:
            msg = ' Processador: i5 7400 3.0Ghz 6MB \n' \
                  ' Memoria Ram: 8Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$2.540,00 \n Acessar o link do PC proposto?'
            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.pichau.com.br/computadores/pichau-home/computador-pichau-home-express-i5-7400-ram-8gb-hd-1tb-400w-bg-024-monitor-21-5-led-full-hd')
            else:
                exit()

if escolha == perfis[2]:

    valores = ["1.000 a 1.800", "1.800 a 2.900"]
    valor = ei.choicebox("Esoolha a faixa de valor que esta disposto a pagar",
                             "PC Finder",
                             valores)

    variacoes = ["Com monitor", "Sem monitor"]
    variacao = ei.choicebox("Escolha seu modelo de preferência:",
                            "Computador ideal",
                            variacoes)

    if valor == "1.000 a 1.800"  :
        if variacao == "Com monitor":
            msg = ' Processador: Celeron G3900 2.8Ghz 2MB \n' \
                  ' Memoria Ram: 4Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$1.414,49 \n Acessar o link do PC proposto?'
            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.pichau.com.br/computadores/pichau-home/computador-pichau-home-express-g3900-2-80ghz-4gb-ddr4-1tb-wisecase-monitor-21-5-led-full-hd')
            else:
                exit()

        if variacao == "Sem monitor":
            msg = ' Processador: Celeron G3930 2.9 Ghz 2MB \n' \
                  ' Memoria Ram: 4Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$939,93 \n Acessar o link do PC proposto?'
            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.pichau.com.br/computadores/pichau-home/computador-pichau-home-express-g3930-2-9ghz-4gb-ddr4-1tb-wisecase')
            else:
                exit()

    if valor == "1.800 a 2.900":
        if variacao == "Com monitor":
                msg = ' Processador: I7 7700 3.6Ghz 8MB \n' \
                      ' Memoria Ram: 8Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$2.896,16 \n Acessar o link do PC proposto?'
                yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
                if yn == 1:
                    webb.open(
                        'https://www.pichau.com.br/computadores/pichau-home/computador-pichau-home-express-i7-7700-3-6ghz-8gb-ddr4-1tb-wisecase-monitor-21-5-led-full-hd')
                else:
                    exit()

        if variacao == "Sem monitor":
             msg = ' Processador: I7 7700 3.6Ghz 8MB \n' \
                              ' Memoria Ram: 8Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$2.432,56 \n Acessar o link do PC proposto?'
             yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
             if yn == 1:
                webb.open(
                        'https://www.pichau.com.br/computadores/pichau-home/computador-pichau-home-express-i7-7700-3-6ghz-8gb-ddr4-1tb-wisecase')
             else:
                exit()

if escolha == perfis[3]:
    modelos = ["MAC OS", "WINDOWS"]
    tipo = ei.choicebox("Esoolha o sistema operacional desejado",title,
                             modelos)

    if tipo == "MAC OS":

        valores = ["7.000 a 12.000", "12.000 a 18.000"]
        variacao = ei.choicebox("Escolha quanto esta disposto a pagar",title,
                                valores)
        if variacao == "7.000 a 12.000":
            msg = ' Processador: I5 7ªgeracao  3.0Ghz \n' \
                  ' Memoria Ram: 8Gb \n Disco Rigido: 1 Tb\n ' \
                  ' Placa de video: Radeon Pro 555 2 Gb \n ' \
                  ' Preço: R$9.799,00 \n Acessar o link do PC proposto?' \

            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.apple.com/br/shop/buy-mac/imac/21,5-polegadas')
            else:
                exit()

        if variacao == "12.000 a 18.000":
            msg = ' Processador: I5 7ªgeracao  3.5Ghz \n' \
                  ' Memoria Ram: 8Gb \n Disco Rigido: 1 Tb\n ' \
                  ' Placa de video: Radeon Pro 575 4 Gb \n ' \
                  ' Preço: R$15.299,00 \n Acessar o link do PC proposto?' \

            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.apple.com/br/shop/buy-mac/imac/27-polegadas')
            else:
               exit()

    if tipo == "WINDOWS":
        valores = ["2.000 a 4.000", "4.000 a 8.000"]
        variacao = ei.choicebox("Escolha quanto esta disposto a pagar", title,
                                valores)
        if variacao == "2.000 a 4.000":
                msg = ' Processador: I3 7100 3.9Ghz 3MB \n' \
                      ' Memoria Ram: 8Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$2.425,00 \n ' \
                      ' Placa de video: Quadro P400 \n ' \
                      ' Acessar o link do PC proposto?'
                yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
                if yn == 1:
                    webb.open(
                        'https://www.pichau.com.br/computadores/pichau-workstation/computador-pichau-workstation-intel-i3-7100-quadro-p400-8gb-ram-1tb-430w-carbide-270r')
                else:
                    exit()

        if variacao == "4.000 a 8.000":
            msg = ' Processador: I7 7700 3.6Ghz 8MB \n' \
                  ' Memoria Ram: 16Gb DDR4 \n Disco Rigido: 1 Tb\n\n Preço: R$7.734,99 \n ' \
                  ' Placa de video: Quadro P4000 \n ' \
                  ' Acessar o link do PC proposto?'
            yn = ei.ynbox(msg, "Abrir o link", choices=['Sim', 'Não'])
            if yn == 1:
                webb.open(
                    'https://www.pichau.com.br/computadores/pichau-workstation/computador-pichau-workstation-intel-i7-7700-quadro-p4000-16gb-ram-1tb-500w-carbide-270r')
            else:
                exit()
