@echo off

REM Root directory
@REM set ROOT=distributed_web_cache
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\core"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\examples"
call :create_folder "%ROOT%\exceptions"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\storage"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\utils"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\config\defaults.py"
call :create_py_file "%ROOT%\config\engine_config.py"

call :create_py_file "%ROOT%\core\cache_node.py"
call :create_py_file "%ROOT%\core\cache_controller.py"
call :create_py_file "%ROOT%\core\eviction.py"
call :create_py_file "%ROOT%\core\distributed_cache.py"

call :create_py_file "%ROOT%\examples\basic_cache.py"
call :create_py_file "%ROOT%\examples\distributed_demo.py"
call :create_py_file "%ROOT%\examples\interactive_cli.py"

call :create_py_file "%ROOT%\exceptions\erros.py"

call :create_py_file "%ROOT%\storage\frequency_storage.py"

call :create_py_file "%ROOT%\tests\test_cache_node.py"
call :create_py_file "%ROOT%\tests\test_distributed_cache.py"
call :create_py_file "%ROOT%\tests\test_eviction.py"
call :create_py_file "%ROOT%\tests\test_frequency.py"
call :create_py_file "%ROOT%\tests\test_utils.py"

call :create_py_file "%ROOT%\utils\logging.py"
call :create_py_file "%ROOT%\utils\normalizer.py"
call :create_py_file "%ROOT%\utils\validators.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\logs\tool_execution.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Distributed Web Cache Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Distributed Web Cache - HTTP caching layer with eviction policies ^(LRU/LFU^)
echo #                   Skills: networking, caching algorithms, concurrency
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b