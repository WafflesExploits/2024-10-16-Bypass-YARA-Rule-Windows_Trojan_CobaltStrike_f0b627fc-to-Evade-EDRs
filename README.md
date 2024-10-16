## Repository of scripts from my blog post
The blog post teaches how to bypass the YARA rule Windows_Trojan_CobaltStrike_f0b627fc.

#### [random_replace_bytes.py](https://github.com/WafflesExploits/CobaltStrike-YARA-Bypass-f0b627fc/blob/main/random_replace_bytes.py) - Made by me
-> Generates alternative shellcode sequences with NOPs bytes to replace signature bytes in Cobalt Strike's .bin file, bypassing the YARA rule Windows_Trojan_CobaltStrike_f0b627fc.

<img width="549" height="150" alt="Usage Example" src="https://github.com/user-attachments/assets/7b4c456c-5455-4314-9665-ac10d457f491">

#### [generate_rich_header.py](https://github.com/WafflesExploits/CobaltStrike-YARA-Bypass-f0b627fc/blob/main/generate_rich_header.py) - Made by [White Knight Labs](https://whiteknightlabs.com/2023/05/23/unleashing-the-unseen-harnessing-the-power-of-cobalt-strike-profiles-for-edr-evasion/) with minor improvements by me
-> Generates Rich header with junk assembly code. 

<img src="https://github.com/user-attachments/assets/e294cdc8-eb15-4744-94f5-410f013c2617" alt="rich header usage example" width="407" height="102">

#### [generate_prepend_headers.py](https://github.com/WafflesExploits/CobaltStrike-YARA-Bypass-f0b627fc/blob/main/generate_prepend_headers.py) - Made by [White Knight Labs](https://whiteknightlabs.com/2023/05/23/unleashing-the-unseen-harnessing-the-power-of-cobalt-strike-profiles-for-edr-evasion/) with minor improvements by me
-> Generates prepend headers with random NOP assembly code.

<img src="https://github.com/user-attachments/assets/25b21f17-8514-4ba9-b685-e9cc85a498a3" alt="prepend header usage example" width="565" height="95">



