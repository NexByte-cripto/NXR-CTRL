# NXR CTRL 6.1 — REDLINE COCKPIT

**Aplicativo experimental e independente para Windows 10/11, com interface PySide6.**

A versão **6.1 é uma reconstrução da interface**, não uma simples recoloração da 6.0.

## Mudança visual — prova verificável

- Barra lateral de ícones de **74 px** (substitui a antiga coluna larga de menu).
- **13 abas horizontais**; instrumentos circulares de CPU e RAM; gráficos de utilização.
- Dashboard horizontal com modos Competitivo, Equilibrado, Cinemático e OC Center.
- Boost em cartões, telas de energia/processos/sensores/FPS/rede e central de comandos em duas colunas.
- Núcleo preservado, nova interface em `nxr_cockpit.py`, iniciada por `nxr_gui.py`.

**[Baixar imagem real da nova interface — artifact do teste no Windows](https://github.com/NexByte-cripto/NXR-CTRL/actions/runs/41155554975)**: seção **Artifacts**, arquivo `NXR-CTRL-6.1-REAL-DASHBOARD`. Capturada durante o teste Qt (sem monitor físico), não é mockup.

## Download oficial

- [Releases](https://github.com/NexByte-cripto/NXR-CTRL/releases)
- [Build Windows 6.1 — testes e compilação](https://github.com/NexByte-cripto/NXR-CTRL/actions/runs/41155554975)

O executável `NXR_CTRL_6_1.exe` só é publicado quando o build termina com sucesso. É um **.exe portátil**, não instalador e não assinado digitalmente.

## Funções

- Leituras locais de CPU, RAM, clocks e uso de disco; temperaturas via LibreHardwareMonitor/OpenHardwareMonitor WMI quando disponíveis.
- Modo de Jogo, Game DVR, planos de energia, restauração de ajustes registrados.
- Processos: visualização e encerramento individual confirmado, com proteção de nomes de processos críticos.
- FPS: CSV PresentMon, antes/depois, 1% low e p99; **sem overlay próprio**.
- Perfis de jogos, rede por teste de conexão TCP, DNS, testes interativos de mouse/teclado e padrões de cor do monitor.
- Comparador de GPUs apenas com resultados de benchmarks importados por CSV e com fonte declarada.
- Central de **44 operações auditáveis**; consulta do mecanismo, limitações e riscos; lote somente de leituras seguras.

## Validação

51 testes do código e smoke test Qt para as 13 telas no Windows. O teste também salva imagem do dashboard real. Isso não substitui testes na sua CPU/GPU e nos drivers locais.

## Transparência

O NXR não recuperou nem copiou código interno de Galdino Control. Overclock, controle de voltagens e ventoinhas não são implementados diretamente; o NXR apenas abre ferramentas de fabricante compatíveis. FPS/temperaturas não são inventados. Alterações potencialmente disruptivas exigem confirmação e devem ser verificadas no seu Windows.
