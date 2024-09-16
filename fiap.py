print("O desenvolvimento desse programa teve como foco o estado de são paulo e os dados apresentados são uma mescla de dados reias e ficticios)")
while True:
    print("\n ======Menu de Culturas Agrícolas======")
    print("1. Cultura de Hortalisas - Tomate")
    print("2. Cultura de Grãos - café")
    print("3. Sair")
    opecao= input("Escolha uma opção: ")
    if opecao == "1":
        while True:
            print("\n ======Menu Tomte======")
            print("1. Informações gerais")
            print("2. Estruta e componentes da orta")
            print("3. Médias e Desvios")
            print("s. Sair")
            op = input("Escolha uma opção: ")
            if op == "1":
                print("oi")
            elif op == "2":
                # area total, area util, numero de ruas e numero de mudas
                print("As mudas possuem um espaçamento de 1m entro elas e para cada 10.000 a plantatação possui 50 ruas de 1 metro de comprimento")
                area_t = float(input("Digite a área disponivel para plantação em m²: "))
                area_ut = area_t * 0.25
                num_rua = (area_t / 10000) * 50
                print(f"A área util da plantação é {area_ut:.2f} m²")
                print(f"O número de ruas da plantação é de {num_rua:.2f} ruas")
                # fase 1 
                print("A primeira fase da plantação de tomate  daura 1 mês e conciste na plantação das mudas e por sua vez no estabelecimento da mesma no solo. \n Os insumos necessários nessa fase são:  as mudas, o adubo de base,  o calcárrio para corrigir o ph do solo e a água")
                print("O ph médio do solo de sp é de 5 e o ph ideal para o tomte é 5,5 a 6,5, para tal vamos calcular quanto de cácario será necessário para que solo passe a ter o ph desejado, esse procedimento é chamdo de calagem")
                    # Numero de mudas
                num_mudas = area_t * 2
                    # calculo da quantidade de calcário(calcário (tonelada/ hectar ): calcário = (V2(percentual de saturação a ser atingido) – V1(percentual de saturação antes da clagem)).T(capacidade de troca catiônica do solo)/PRNT ((Poder Relativo de Neutralização Total do Calcário)
                    # V2 - percentual de saturação a ser atingido | V1 - percentual de saturação antes da clagem | T - capacidade de troca catiônica do solo | PRNT - Poder Relativo de Neutralização Total do Calcário 
                    # cal = (v2 - v1) * t/prnt
                v1 = 0.5 # 0.5 = 50%
                v2 = 0.75 # 0.75 = 75%
                t = 50
                prnt = 0.7 # 0.7 = 70%
                cal = ((v2 - v1) * t/prnt) * (area_t/10000) # a rea total deve ser dividida por 10000 para obetermos a quantidade de hetares para efetuarmos o calculo
                    # quantide de necessária de adubo de base - 0,85 kg/m²
                adubo_base = 0,85 * area_t
                    # Quantidade de água 
                ir1_dia = 5*area_t
                ir1_semana = ir1_dia * 7
                ir1_mês = ir1_semana * 4
                print("É importante relembrar que o ideal para o tomate é ser irrigado em dois períodos, para tal a quantidade diária de água deve ser dividida por 2, tendo uma irrigação de manha e uma de noite")
                print(f"O número de mudas  a serem platadas é de {num_mudas:.2f} mudas")
                print(f"A quantidade de calcário necessária para corrigir o ph do solo em toneldas é de {cal:.2f}t ")
                print(f"A quantidade de adubo necessária é de {adubo_base:.2f} kg de adubo")
                print(f"A quantidade de agá utlizada por dia é de {ir1_dia:2f} L, por semana é {ir1_semana:.2f} L e por mês é{ir1_mês:.2f} ")
                print(f"Na primeira fase sera utlizado no total {ir1_mês:.2f} L de água ")
                # fase 2 
                print("A segunda fase dura 2 mêses e conciste no crescimento vegetativo, ou seja, desenvolvimento da muda, pé de tomate. \n Os insumos necessários nessa fase são: o adubo foliar, fertilizante, fungicida (1° Aplicação), inseticida (1° Aplicação) e água ")
                print("É importante reslatar que tanto o inseticida quanto o funcida são divididos em 2 aplicações, além disso a segunda aplicação é masi fraca em relação a primeira, sendo a primeira aplicação no ínicio da segunda fase e a segunda alicação no ultimo mês da terceira fase \n além disso o inseticida, o fungicida o fertilizante devem ser pulverizados com axulio de maquinas, como drone e trator pulverizante")
                    #  adubo foliar deve ser utilizado 1 kg para cada 10m² 
                adubo_foliar = (area_t/10) * 1 
                fertilizante = 0.7 * area_t
                fung_ap1 = 1.5 * (area_t/10000)
                incet_ap1 = 1.5 * (area_t/10000)
                    # irrigação
                ir2_dia = 8*area_t
                ir2_semana = ir2_dia * 7
                ir2_mês = ir2_semana * 4
                ir2_total = ir2_mês * 2 
                print(f"A cuntidade necessária de adubo foliar é de {adubo_foliar:.2f} kg")
                print(f"A quabtidade necessária de fertilizante é de {fertilizante:.2f} kg")
                print(f"A quantidade necessária de fungicida para a 1° aplicação é de {fung_ap1:.2f} L")
                print(f"A quantidade necessária de inseticida para a 1° aplicação é de {incet_ap1:.2f} L")
                print(f"A quantidade de agá utlizada por dia é de {ir2_dia:2f} L, por semana é {ir2_semana:.2f} L e por mês é{ir2_mês:.2f} ")
                print(f"Na segunda faze sera utlizado no total {ir2_total} L de água ")
                # fase 3
                print("A terceira fase dura 2 mêses e conciste na floração e frutificação, ou seja, desenvolvimento da das flores e dos frutos \n Os insumos necessários nessa fase são: o adubo foliar, fertilizante, fungicida (2° Aplicação), inseticida(2° Aplicação) e água ")
                print(" Lembrando  que no  segundo mês da 3° fase da  deve ser realizada a segunda aplicação de fungicida e inseticida")
                    #  adubo foliar deve ser utilizado 1 kg para cada 10m² 
                adubo_foliar = (area_t/10) * 1 
                fertilizante = 0.7 * area_t
                fung_ap1 = 1.0 * (area_t/10000)
                incet_ap1 = 1.0 * (area_t/10000)
                    # irrigação
                ir3_dia = 8*area_t
                ir3_semana = ir3_dia * 7
                ir3_mês = ir3_semana * 4
                ir3_total = ir3_mês * 2 
                print(f"A cuntidade necessária de adubo foliar é de {adubo_foliar:.2f} kg")
                print(f"A quabtidade necessária de fertilizante é de {fertilizante:.2f} kg")
                print(f"A quantidade necessária de fungicida para a 1° aplicação é de {fung_ap1:.2f} L")
                print(f"A quantidade necessária de inseticida para a 1° aplicação é de {incet_ap1:.2f} L")
                print(f"A quantidade de agá utlizada por dia é de {ir3_dia:2f} L, por semana é {ir3_semana:.2f} L e por mês é{ir3_mês:.2f} ")
                print(f"Na terceira fase sera utlizado no total {ir3_total} L de água ")
                # fase 4 
                print("A quarta fase conciste na maturação e colheita do tomate que dura 1 mês em média e para essa fase o único insumo necessário é água")
                    #5L/m² - dia
                ir4_dia = 5*area_t
                ir4_semana = ir4_dia * 7
                ir4_mês = ir4_semana * 4
                print(f"Na quarta fase sera utlizado no total {ir4_mês} L de água ")
                #Conciderações Finais
                Ir_total = ir1_mês + ir2_total + ir3_total + ir4_mês
                num_total_de_tomates = 5 * num_mudas
                print(f"A quantidade total de água utlizada em um ciclo completo do tomate é de {Ir_total:.2f} L de água")
                print(f"Num clico completo do tomate são produzidos {num_total_de_tomates:.2f} kg de tomate")
                print(" Foi calculado todos os insumo necessários para o estabelecimento e cultura do tomate")
            elif op == "3":
        
                
                

