#!/bin/sh

wget -nv -O script_encoded.js http://www.enigmagroup.org/missions/basics/js/8/script.js
perl JScript.decode-1.0.pl script_encoded.js script_decoded.js
echo "in decoded form:"
cat script_decoded.js && echo
echo "106,111,104,110,110,121  /  107,101,98,97,98"
echo " j   o   h   n   n   y       k   e   b  a  b"
rm -f script_*.js
echo "so you go to kebab.php to solve this challenge"
