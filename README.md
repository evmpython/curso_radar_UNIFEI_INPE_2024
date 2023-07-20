# **Curso:** *Radar Meteorológico: fundamentos e aplicações*

---

**OBJETIVO:** A parte prática do curso tem como objetivo ensinar aos alunos como processar e plotar dados de radares meteorológicos.

---

**EMENTA**: Será abordado os seguintes tópicos.

1. Conhecendo os dados de radar
2. Estratégia de varredura
3. Plan Position Indicator (PPI)
4. Seção transversal vertical
5. Constant Altitude Plan Position Indicator (CAPPI)
6. Estimativa de precipitação
7. Classificação de hidrometeoros
8. Classificação convectiva/estratiforme
9. Perfis verticais
10. Vento radial
11. Rastreamento automático de sistemas precipitantes
12. Combinação de mapa de radar e relâmpagos
13. Biblioteca ProPlot
---

**DADOS:** A parte prática do curso usará como dados de entrada os dados voluméticos em formato HDF5 do radar de Salesópolis. Esses dados de radar são referentes ao desastre natural que provocou as [**Enchentes e deslizamentos de terra no Litoral Norte de São Paulo entre os dias 18 e 19 de fevereiro de 2023**](https://pt.wikipedia.org/wiki/Enchentes_e_deslizamentos_de_terra_no_Litoral_Norte_de_S%C3%A3o_Paulo_em_2023). Este evento afetou as cidades de Ubatuba, São Sebastião, Guarujá, Ilhabela, Caraguatatuba e Bertioga e produziu precipitação histórica de **680 mm em 9 h**, provocando a morte de **65 pessoas (64 em São Sebastião e 1 em Ubatuba)**.

---

**PROCEDIMENTO REALIZADO:** Os seguintes procedimentos são realizados nesse código:
1. 1° Passo: Instalando bibliotecas
2. 2° Passo: Importando bibliotecas
3. 3° Passo: Criando diretório de entrada e saída
4. 4° Passo: Download dos dados de Radar, Relevo, Relâmpagos e Municípios
5. 5° Passo: Download dos dados de shapefiles
6. 6° Passo: Declarando funções
7. Informações sobre as bibliotecas Py-ART e Wradlib
8. **Script 01** - Conhecendo os dados do radar com o Py-ART
9. **Script 02** - Plotando a estratégia de varredura do radar
10. **Script 03** - Plotando Plan Position Indicator (PPI) de ZH, ZDR, KDP e COR
11. **Script 04** - Plotando Plan Position Indicatior (PPI) de Vento Radial
12. **Script 05** - Plotando Vários Plan Position Indicator (PPI) de Refletividade
13. **Script 06** - Plotando Uma Seção Transversal
14. **Script 07** - Gerando e plotando CAPPI
15. **Script 08** - Escrevendo e Lendo dado de CAPPI gerado
16. **Script 09** - Estimativa de Precipitação
17. **Script 10** - Classificação de hidrometeoros
18. **Script 11** - Classificação Convectiva/Estratiforme
19. **Script 12** - Seção transversal a partir do CAPPI
20. **Script 13** - Máxima refletividade
21. **Script 14** - Perfil vertical
22. **Script 15** - Rastreamento de tempestades com o TATHU
23. **Script 16** - Combinação de mapa de radar e GLM (GOES-16)
24. **Script 17** - Plotando gráficos com Proplot - Região de estudo
25. **Script 18** - Plotando gráficos com Proplot - CAPPI de refletividade
26. **Script 19** - Plotando gráficos com Proplot - CAPPI de refletividade de todos horários
27. **Script 20** - Plotando gráficos com Proplot - Animação de CAPPI
28. **Script 21** - Plotando gráficos com Proplot - Figura com subplots
29. **Script 22** - Plotando gráficos com Proplot - Combinação de mapa de radar e relâmpagos
30. **Script 23** - Plotando gráficos com Proplot - Combinação de mapa de radar e relâmpagos para diversos horários e com animação
31. **Script 24** - Plotando gráficos com Proplot - Ciclo diurno de relâmpagos
32. **Script 25** - Plotando gráficos com Proplot - Ciclo a cada 5 min de relâmpagos



---

**OBSERVAÇÕES IMPORTANTES**:
1. Este código foi desenvolvido para ser processado no [Google Colaboratory](https://colab.research.google.com/).

---

**Equipe:**
 - Diego Souza - INPE: diego.souza@inpe.br
 - Enrique Vieira Mattos - UNIFEI: enrique@unifei.edu.br
 - Thiago Souza Biscaro - INPE: thiago.biscaro@inpe.br

---
