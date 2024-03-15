
#`Sejam bem-vindos ao curso!`

- Este Colab contêm as informações para instalar as bibliotecas necessárias e os scritps em Python para manipular os dados de radar meteorológico.

- Todas as instruções e scripts são processados diretamente na nuvem, não sendo necessário instalar ferramentas ou fazer o download dos dados localmente no seu computador. Para rodar as células de código, click no ícone de `play` no lado esquerdo superior ou digite `shift enter` no seu teclado.

- ---
#CURSO: **RADAR METEOROLÓGICO: FUNDAMENTOS E PROCESSAMENTO DE DADOS COM PYTHON**

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
11. Combinação de mapa de radar e relâmpagos
12. Biblioteca ProPlot
13. Biblioteca Xradar
---

**DADOS:** A parte prática do curso usará como informações de entrada os dados voluméticos em formato HDF5 do radar de [Salesópolis](https://www.saisp.br/estaticos/sitenovo/home.html). Esses dados de radar são referentes ao desastre natural que provocou as [**Enchentes e deslizamentos de terra no Litoral Norte de São Paulo entre os dias 18 e 19 de fevereiro de 2023**](https://floodlist.com/america/brazil-floods-sao-paulo-february-2023). Este evento foi [histórico](https://www.bbc.com/portuguese/articles/cydngmz112mo) e afetou as cidades de Ubatuba, São Sebastião, Guarujá, Ilhabela, Caraguatatuba e Bertioga e produziu precipitação de **680 mm em 24 h**, provocando a morte de [**65 pessoas (64 em São Sebastião e 1 em Ubatuba)**](https://pt.wikipedia.org/wiki/Enchentes_e_deslizamentos_de_terra_no_Litoral_Norte_de_S%C3%A3o_Paulo_em_2023).

---

**PROCEDIMENTO REALIZADO:** Os seguintes procedimentos serão realizados na parte prática desse curso:
1. 1° Passo: Instalando bibliotecas
2. 2° Passo: Importando bibliotecas
3. 3° Passo: Criando diretório de entrada e saída
4. 4° Passo: Download dos dados de entrada
5. 5° Passo: Declarando funções
6. Informações sobre as bibliotecas Py-ART e Wradlib
7. **Script 01** - Conhecendo os dados do radar com o Py-ART
8. **Script 02** - Plotando a estratégia de varredura do radar
9. **Script 03** - Plotando Plan Position Indicator (PPI) de ZH, ZDR, KDP e COR
10. **Script 04** - Plotando Plan Position Indicatior (PPI) de vento radial
11. **Script 05** - Plotando Vários Plan Position Indicator (PPI) de refletividade
12. **Script 06** - Plotando uma seção transversal vertical
13. **Script 07** - Gerando e plotando Constant Altitude Plan Position Indicator (CAPPI)
14. **Script 08** - Escrevendo e lendo dado de CAPPI gerado
15. **Script 09** - Estimativa de precipitação
16. **Script 10** - Classificação de hidrometeoros
17. **Script 11** - Classificação convectivo/estratiforme
18. **Script 12** - Seção vertical ao longo de uma latitude e longitude
20. **Script 13** - Seção transversal a partir do CAPPI
21. **Script 14** - Máxima refletividade
22. **Script 15** - Perfil vertical das variáveis polarimétricas
23. **Script 16** - Perfil vertical de vento
24. **Script 17** - Combinação de mapa de radar e GLM (GOES-16)
25. **Script 18** - Plotando gráficos com Proplot - Conhecendo a Biblioteca
26. **Script 19** - Plotando gráficos com Proplot - Baixando os dados necessários
27. **Script 20** - Plotando gráficos com Proplot - Região de estudo
28. **Script 21** - Plotando gráficos com Proplot - CAPPI de refletividade
28. **Script 22** - Plotando gráficos com Proplot - CAPPI de refletividade de todos horários
29. **Script 23** - Plotando gráficos com Proplot - Animação de CAPPI
30. **Script 24** - Plotando gráficos com Proplot - Figura com subplots
31. **Script 25** - Plotando gráficos com Proplot - Combinação de mapa de
radar e relâmpagos
32. **Script 26** - Plotando gráficos com Proplot - Combinação de mapa de radar com Zoom e relâmpagos
33. **Script 27** - Plotando gráficos com Proplot - Combinação de mapa de radar e relâmpagos para diversos horários e com animação
34. **Script 28** - Plotando gráficos com Proplot - Ciclo diurno de relâmpagos
35. **Script 29** - Plotando gráficos com Proplot - Ciclo a cada 5 min de relâmpagos
36. **Script 30** - Introduzindo a biblioteca Xradar
---

**OBSERVAÇÕES IMPORTANTES**:
1. Este código foi desenvolvido para ser processado no [Google Colaboratory](https://colab.research.google.com/).
2. Os dados estão disponíveis no [github do curso](https://github.com/evmpython/curso_radar_UNIFEI_INPE_2024).

---

**Equipe:**

Palestrantes/Tutores:

 - Enrique Vieira Mattos - UNIFEI: enrique@unifei.edu.br / https://github.com/evmpython
 - Thiago Souza Biscaro - INPE: thiago.biscaro@inpe.br / https://github.com/tsbiscaro

Colaboradores:
 - Diego Souza - INPE: diego.souza@inpe.br / https://github.com/diegormsouza
 - Flávio Augusto - UNIFEI: augustoflaviobob@gmail.com
---
