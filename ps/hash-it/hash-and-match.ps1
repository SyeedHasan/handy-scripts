Get-ChildItem C:\ -Recurse | Get-FileHash -Algorithm SHA256 | Where-Object Hash -eq {HashToMatch} | Select Path