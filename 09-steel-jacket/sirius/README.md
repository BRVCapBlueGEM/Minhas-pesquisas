# Sirius: conversão de pixel para coordenada

A Carta Sirius tem um **quadriculado geográfico impresso**, com cruzamentos rotulados em graus e minutos (32°25′, 32°35′, 30°20′, 30°25′, 30°35′…). Esses cruzamentos são os pontos de controle, porque a coordenada deles é exata e não depende de identificar nenhuma feição.

O carimbo verde no centro da carta diz, em hebraico, que as minas estão "atualizadas até 1/10/73" e que foram marcadas "somente em território inimigo". A carta mostra, portanto, a situação de cinco dias antes da guerra.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `gcp_sirius.csv` | Cruzamentos do quadriculado: pixel → longitude/latitude, separados por folha do mosaico |
| `pontos_sirius_px.csv` | Pontos marcados na Sirius, em pixel. **Editar aqui.** |
| `pontos_sirius_convertidos.csv` | Gerado por `scripts/sirius_converter.py`. Não editar. |

## Pixels de referência

Os pixels são do recorte `SIRIUS_recorte_X1500-4500_Y6500-9500_q96.jpg`, com 2576 × 2576 px. Ele corresponde à região X 1500–4500, Y 6500–9500 da `SIRIUS_COMPLETA_COMMONS.jpg` (6784 × 15819 px), reduzida para 2576 px. O script converte e informa também o pixel na Sirius completa.

Confirmação: o forte de Lakekan, medido no recorte, cai em (2787, 8338) da Sirius completa. O registro do projeto de 3/10/2026 indicava (2786, 8339).

## Folhas do mosaico

A Sirius é feita de várias folhas emendadas. Neste recorte há uma emenda horizontal, na altura de Missouri, perto do Y 905 do recorte.

- **Folha inferior** (Matzmed, Lakekan, Amir e o Grande Lago Amargo): 4 cruzamentos. Escala de cerca de 17,5 m por pixel do recorte.
- **Folha superior** (Missouri e o norte): só 2 cruzamentos neste recorte, na linha 30°35′N. **Ainda não dá para converter.** É preciso pelo menos um cruzamento a mais, que fica fora do recorte, mais ao norte.

As duas folhas não coincidem. O meridiano 32°35′ está em X 2096 acima da emenda e em X 2086 abaixo dela. Por isso cada folha tem sua própria transformação.

## Precisão

- Os quatro cruzamentos da folha inferior formam um paralelogramo quase perfeito, por isso o resíduo do ajuste afim é zero. Isso não comprova a precisão: com 4 pontos sobra só um grau de liberdade.
- Marcação manual dos pixels: ±2 px, ou seja, ±35 m.
- O datum da Sirius não foi identificado. A diferença para o WGS84 deve ficar na casa de algumas centenas de metros, abaixo do hexágono de 1 km.
- Por isso os pontos da Sirius entram com grau **B** e incerteza de 250 m.

## Resultado das conferências

| Ponto | Sirius | Referência anterior | Diferença |
|---|---|---|---|
| Matzmed | 30.41519, 32.35735 | P01 do projeto: 30.423143, 32.361259 | 0,96 km |
| Fazenda Chinesa (Amir) | 30.46029, 32.38307 | Wikipedia: 30°27′N 32°24′E, arredondada ao minuto | 2,0 km |
| Matzmed → Lakekan | 5,0 km para sudeste | Afirmação "8 km ao norte" | Distância e direção não conferem |
