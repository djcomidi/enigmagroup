#!/bin/sh

echo "IP ADDRESS:"
ip=$(nslookup enigmagroup.org | sed -n '6p' | cut -d ' ' -f 2)
echo "\t$ip"

echo "SERVER:"
server=$(curl -s -I www.enigmagroup.org | grep "^Server:" | cut -d ' ' -f 2)
echo "\t$server"

echo "NAMESERVERS:"
nameservers=$(whois enigmagroup.org | grep "^Name Server:N" | cut -d ':' -f 2)
for ns in $nameservers; do
	echo "\t$ns";
done

echo "TECH NAME:"
techname=$(whois enigmagroup.org | grep "^Tech Name" | cut -d ':' -f 2)
echo "\t$techname"

echo "TECH EMAIL:"
techemail=$(whois enigmagroup.org | grep "^Tech Email" | cut -d ':' -f 2)
echo "\t$techemail"
