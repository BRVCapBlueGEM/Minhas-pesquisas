# Sirius: conversão de pixel para coordenada

A Carta Sirius tem um **quadriculado geográfico impresso**, com linhas a cada 5′ e rótulos em graus e minutos. Os cruzamentos dessas linhas servem de pontos de controle: a coordenada deles é exata e não depende de identificar nenhuma feição.

O carimbo verde no centro da carta diz, em hebraico, que as minas estão "atualizadas até 1/10/73" e que foram marcadas "somente em território inimigo". A carta mostra a situação de cinco dias antes da guerra.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `gcp_sirius.csv` | 24 cruzamentos do quadriculado (pixel → lon/lat), com a folha de cada um |
| `pontos_sirius_px.csv` | Pontos marcados na Sirius. **Editar aqui.** |
| `areas_sirius_px.csv` | Contornos marcados na Sirius, com vértices em ordem. **Editar aqui.** |
| `pontos_sirius_convertidos.csv`, `areas.geojson` | Gerados por `scripts/sirius_converter.py`. Não editar. |

Todos os pixels são da `SIRIUS_COMPLETA_COMMONS.jpg` original (6784 × 15819 px). Eles foram medidos nos blocos de 2000 px sem redução (`SIRIUS_Xnnnn_Ynnnn`) da faixa X 0–6000, Y 4000–10000.

## Folhas do mosaico

A Sirius é feita de folhas emendadas que **não coincidem** nas emendas: o mesmo meridiano aparece até 16 px (cerca de 240 m) deslocado de uma folha para outra. Por isso cada folha tem sua própria transformação, e cada pixel é convertido pela folha onde está.

| Folha | Faixa (pixels) | Cruzamentos | Erro médio | Erro máximo |
|---|---|---|---|---|
| E1 (oeste, norte) | X < 3400, Y 5700–7540 | 6 | 19 m | 27 m |
| E2 (oeste, sul) | X < 3400, Y 7540–9400 | 6 | 16 m | 21 m |
| D1 (leste, norte) | X ≥ 3400, Y 5700–7540 | 6 | 8 m | 10 m |
| D2 (leste, sul) | X ≥ 3400, Y 7540–9400 | 6 | 49 m | 77 m |

Escala: cerca de 67,5 px por km (1 px ≈ 15 m).

## Correção em relação à primeira versão

A primeira conversão usou um recorte reduzido e misturou cruzamentos das folhas E2 e D2. Os pontos se deslocaram até cerca de 120 m com a conversão por folha. Matzmed, Lakekan e a Fazenda Chinesa foram recalculados.

## Precisão

- Marcação dos pixels: ±2 px, ou seja, ±30 m. Somado ao erro do ajuste, fica abaixo de 100 m.
- O datum da Sirius não foi identificado. A diferença para o WGS84 deve ser de algumas centenas de metros, abaixo do hexágono de 1 km.
- Por isso os pontos da Sirius entram com grau **B** e incerteza de 250 m.

## Missouri

O objetivo Missouri (מיסורי) está desenhado na Sirius como um contorno magenta fechado, de cerca de 3,3 × 7,7 km, que atravessa a emenda E1/E2. Ele foi registrado como área (`areas.geojson`), e o ponto em `pontos.csv` é o centro do contorno. Na emenda, o desenho das duas folhas difere em cerca de 120 m.

## Conferência independente com a AMS P502 NH 36-6

O recorte `Steel_Jacket_Ismailia_NH36-6_Recorte.png` da carta norte-americana (anos 1950–60) foi georreferenciado pela quadrícula UTM impressa (quadrados VU, linhas a cada 10 km, zona 36). Foram usados 29 cruzamentos, com erro médio de 24 m e escala de 36 m por pixel. Depois, a Sirius convertida por folha foi projetada sobre ela: `sobreposicao_sirius_nh36-6.jpg`.

Resultado visual: o Grande Lago Amargo, o canal, o Timsah e a Jerusalem Road coincidem nas duas cartas. As diferenças ficam em poucos pixels da NH (cerca de 100–200 m), abaixo do hexágono de 1 km. A NH também confirma que Kishuf é o Gebel Hibeita: o nome aparece no mesmo lugar nas duas cartas.

Limite: a NH tem 36 m por pixel e não identifica o datum. A conferência vale como verificação independente da ordem de grandeza, não como medida de precisão métrica.
