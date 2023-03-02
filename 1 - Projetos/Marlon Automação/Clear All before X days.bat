REM Deletar arquivos com mais de 30 dias

forfiles /p "%UserProfile%\Downloads" /s /m *.* /c "cmd /c Del @path" /d -30