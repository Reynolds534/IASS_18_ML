@ECHO OFF
for %%i in (%1) do (
	if NOT "%%~$PATHLIST:i"=="" (
		ECHO %%~$PATHLIST:i
		SET currentpythonpath=%%~$PATHLIST:i
		FOR /F "delims=" %%j IN ("%currentpythonpath%") DO (
			SET filedrive=%%~dj
			SET filepath=%%~pj
			rem filename=%%~nj
			rem fileextension=%%~xj
			SET scriptpath=%filedrive%%filepath%Scripts
			ECHO %scriptpath%
			SET PATH=%PATH%;%scriptpath%
			)
		)
	)
