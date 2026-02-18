this project analyzes emergency resource request and categorizes them .
reg=enter your register number
pli=reg%5
 rule 1:reg%5==0 remove high demand
 rule 2: reg%5==1 remove low demand
 rule 3: if not both cases then remove invalid_request
 Categorizes requests into Low, Moderate, High, Invalid
- Applies PLI filtering
- Generates final dispatch report
