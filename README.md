# NXR CTRL — Redline Edition

Aplicativo experimental de controle e diagnostico de desempenho no Windows, desenvolvido com Python 3.12, PySide6 e psutil.

## Estado da publicacao

O fluxo **Build NXR CTRL Windows** esta configurado. O repositorio ainda precisa receber **todos os arquivos-fonte** da pasta `NXR_CTRL_5_2_1_REPARO` antes da compilacao funcionar. O instalador/executavel ainda **nao foi publicado**.

## Como enviar os arquivos

1. Na pagina do repositorio, escolha **Add file > Upload files**.
2. Arraste o **conteudo extraido** de `NXR_CTRL_5_2_1_REPARO`, nao o ZIP fechado.
3. Inclua os arquivos `nxr_gui.py`, `nxr_service.py`, `nxr_launcher.py`, `fps_engine.py`, `core.py`, `procore.py`, `ultra_tools.py` e `requirements.txt`.
4. Finalize usando **Commit changes**.

Depois, abra **Actions > Build NXR CTRL Windows**. O workflow inicia quando os arquivos Python forem enviados ou pode ser acionado em **Run workflow**.

Se os testes e a compilacao passarem, o GitHub criara a versao em **Releases** com o arquivo `NXR_CTRL_5_2_1.exe`. Nao ha link funcional de EXE ate a criacao da Release.

### Acesso rapido

- [GitHub Actions](https://github.com/NexByte-cripto/NXR-CTRL/actions)
- [Releases](https://github.com/NexByte-cripto/NXR-CTRL/releases)
- [Upload de arquivos](https://github.com/NexByte-cripto/NXR-CTRL/upload/main)

## Limitacoes

Sem overlay FPS em tempo real ou overclock direto de CPU/GPU. Sensores termicos dependem de software compativel. Software sem assinatura digital. Testar em PC de desenvolvimento antes de usar no sistema principal.
