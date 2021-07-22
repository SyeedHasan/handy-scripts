for /R C:\ %%f in (*.*) do @certutil -hashfile ^"%%f^" SHA1 | find /i /v "certutil" >> %COMPUTERNAME%-results.log

