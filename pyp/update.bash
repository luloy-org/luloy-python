


light_green='\e[1;32m'
yellow='\e[33m'
nc='\e[0m'
echo -e "${yellow}system updating...${nc}"
cd 
rm -rf pyp
git clone https://github.com/reyyymartt/pyp.git
echo -e "${light_green}file updated${nc}"
clear
echo -e "${yellow}System updated!${nc}"
cd pyp
ls
bash start.bash



