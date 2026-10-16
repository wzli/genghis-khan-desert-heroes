@echo off
setlocal
echo ==========================================================
echo  成吉思汗之大漠英雄傳 (Genghis Khan 1999) - Language Switcher
echo ==========================================================
echo  1. Switch to English
echo  2. Switch to Traditional Chinese (Original)
echo ==========================================================
set /p choice="Select option (1 or 2): "

cd /d "%~dp0assets\game"

if "%choice%"=="1" (
    echo Switching to English...
    copy /y text_en\*.txt . >nul
    if exist Hero.exe.en copy /y Hero.exe.en Hero.exe >nul
    if exist mainmenu_en.bmp copy /y mainmenu_en.bmp mainmenu.bmp >nul
    if exist single_en.bmp copy /y single_en.bmp single.bmp >nul
    if exist story_en.bmp copy /y story_en.bmp story.bmp >nul
    if exist stage_en.bmp copy /y stage_en.bmp stage.bmp >nul
    if exist act_bg_en.bmp copy /y act_bg_en.bmp act_bg.bmp >nul
    if exist netmenu00_en.bmp copy /y netmenu00_en.bmp netmenu00.bmp >nul
    if exist netmenu01_en.bmp copy /y netmenu01_en.bmp netmenu01.bmp >nul
    if exist netmenu02_en.bmp copy /y netmenu02_en.bmp netmenu02.bmp >nul
    if exist netmenu03_en.bmp copy /y netmenu03_en.bmp netmenu03.bmp >nul
    if exist selects_en.dat copy /y selects_en.dat selects.dat >nul
    if exist windows_en.dat copy /y windows_en.dat windows.dat >nul
    if exist netGraphics_en.dat (
        copy /y netGraphics_en.dat netGraphics.dat >nul
        copy /y netGraphics_en.dat netgraphics.dat >nul
    )
    if exist stage_en.ini copy /y stage_en.ini stage.ini >nul
    for %%F in (stage*_en.spr) do (
        set "fname=%%~nF"
        copy /y "%%F" "!fname:_en=!%%~xF" >nul
    )
    for %%F in (stage*_en.stg) do (
        set "fname=%%~nF"
        copy /y "%%F" "!fname:_en=!%%~xF" >nul
    )
    echo English > .current_language
    echo [OK] Game language set to English!
) else if "%choice%"=="2" (
    echo Switching to Traditional Chinese...
    copy /y text_zh\*.txt . >nul
    if exist Hero.exe.zh copy /y Hero.exe.zh Hero.exe >nul
    if exist mainmenu_zh.bmp copy /y mainmenu_zh.bmp mainmenu.bmp >nul
    if exist single_zh.bmp copy /y single_zh.bmp single.bmp >nul
    if exist story_zh.bmp copy /y story_zh.bmp story.bmp >nul
    if exist stage_zh.bmp copy /y stage_zh.bmp stage.bmp >nul
    if exist act_bg_zh.bmp copy /y act_bg_zh.bmp act_bg.bmp >nul
    if exist netmenu00_zh.bmp copy /y netmenu00_zh.bmp netmenu00.bmp >nul
    if exist netmenu01_zh.bmp copy /y netmenu01_zh.bmp netmenu01.bmp >nul
    if exist netmenu02_zh.bmp copy /y netmenu02_zh.bmp netmenu02.bmp >nul
    if exist netmenu03_zh.bmp copy /y netmenu03_zh.bmp netmenu03.bmp >nul
    if exist selects_zh.dat copy /y selects_zh.dat selects.dat >nul
    if exist windows_zh.dat copy /y windows_zh.dat windows.dat >nul
    if exist netGraphics_zh.dat (
        copy /y netGraphics_zh.dat netGraphics.dat >nul
        copy /y netGraphics_zh.dat netgraphics.dat >nul
    )
    if exist stage_zh.ini copy /y stage_zh.ini stage.ini >nul
    for %%F in (stage*_zh.spr) do (
        set "fname=%%~nF"
        copy /y "%%F" "!fname:_zh=!%%~xF" >nul
    )
    for %%F in (stage*_zh.stg) do (
        set "fname=%%~nF"
        copy /y "%%F" "!fname:_zh=!%%~xF" >nul
    )
    echo Traditional Chinese > .current_language
    echo [OK] Game language set to Traditional Chinese!
) else (
    echo Invalid choice.
)
pause
