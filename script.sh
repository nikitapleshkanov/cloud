az vm start --name nikitaVM321 --resource-group VM
ssh -i azureNikita pleshkanov@40.121.43.167 python3 main.py
az vm deallocate --resource-group VM --name nikitaVM321
