# NXR CTRL 6.0 — Black Red Edition

Aplicativo independente de diagnóstico e controle de desempenho para Windows 10/11. Interface Qt/PySide6, telemetria local, rede, FPS por CSV e perfis de energia.

## Versões e download

- **[Releases oficiais do projeto](https://github.com/NexByte-cripto/NXR-CTRL/releases)** — arquivos executáveis quando a compilação Windows terminar com sucesso.
- **[Compilação Black Red 6.0](https://github.com/NexByte-cripto/NXR-CTRL/actions/workflows/black-red-60.yml)** — testes automatizados e compilação do `.exe`.
- **[Código-fonte 6.0 versionado](https://github.com/NexByte-cripto/NXR-CTRL/blob/main/source/nxr_6_0.tar.br.base64)** — arquivo técnico comprimido; extraído automaticamente no workflow.
- **[Script de extração](https://github.com/NexByte-cripto/NXR-CTRL/blob/main/scripts/unpack60.py)**.

**Não é necessário enviar ZIPs nem instalar Python para usar um .exe compilado**, mas o download de uma nova versão só estará disponível quando a ação do GitHub terminar e a Release for publicada. O arquivo resultante é portável, não um instalador Inno Setup.

## O que o NXR CTRL 6.0 faz

- Dashboard com dados locais de CPU, RAM e discos.
- Diagnósticos de GPU, drivers, clocks e sensores quando há integração WMI compatível.
- **44 operações auditáveis em 10 áreas**, indicando mecanismo, risco, requisitos e reversibilidade.
- Botão de diagnóstico seguro em lote: apenas **seis leituras**, sem alterar Windows ou encerrar processos.
- Planos de energia e Modo de Jogo com confirmação.
- Processos, rede, testes de mouse/teclado/monitor e comparação de GPUs via CSV com fontes.
- FPS por CSV PresentMon; não implementa overlay de FPS próprio.
- Integrações com aplicações de fabricante para overclock, sem escrita direta de clocks ou tensões.

## Originalidade e limites

A inspeção estática do instalador do Galdino Control foi utilizada apenas para identificar o **tipo de instalador (Inno Setup 6.7)** e elementos de empacotamento. **Os comandos e o código-fonte internos do Galdino não foram recuperados nem copiados.** A implementação do NXR CTRL é independente.

Não promete 100 FPS em qualquer hardware nem ganhos não medidos. Não desativa Windows Defender, UAC ou serviços críticos automaticamente. Software experimental e não assinado digitalmente, com validação em hardware real ainda pendente.

## Testes

O núcleo da versão 6.0 passou por **48 testes automatizados** no ambiente de desenvolvimento. O workflow Windows deve executar os mesmos testes e um teste de abertura de todas as 13 telas Qt antes de compilar o executável.
