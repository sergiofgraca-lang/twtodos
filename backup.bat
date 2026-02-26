@echo off
set data=%date:~6,4%-%date:~3,2%-%date:~0,2%
copy db.sqlite3 backup\db_%data%.sqlite3
echo Backup criado com sucesso!
pause